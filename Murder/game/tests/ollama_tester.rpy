# Local-LLM beta tester: lets a model running on Ollama pick the game's choices.
#
# The real game runs under Ren'Py's test runner (renpy.is_in_test() is True), so
# TimedMenu.display_choices() already delegates every choice to
# test.autorunner.pick_choice_for_menu(). When autorunner.ollama_mode is True that
# method calls decide_choice() below instead of consuming a recorded JSON plan.
#
# The model "sees" the dialogue through the transcript Ren'Py already accumulates in
# _history_list (rendered by _transcript_lines() in custom_functions.rpy) and replies
# with a JSON {"choice": <index>, "reason": <text>} picking one of the valid options.
#
# Launch (Ollama must be serving the model first):
#     ollama serve            # and: ollama pull gemma3:12b
#     renpy.exe  <project>  --test captain.ollama_friday_evening
#
# Artifacts per run land next to the transcript under tests/result/<text_id>/<chapter>/.

init python in test:
    import json
    import os
    import datetime
    import urllib.request
    import urllib.error

    import renpy.exports as renpy

    # ------------------------------------------------------------------ config
    # Confirm the exact model tag with `ollama list` and edit if needed.
    OLLAMA_URL = "http://localhost:11434/api/chat"
    OLLAMA_MODEL = "gemma4:12b-it-qat"
    OLLAMA_TIMEOUT = 30          # seconds; keep well under the 180s test Until
    TEMPERATURE = 0.6            # low-ish: plausible but not deterministic
    TRANSCRIPT_TAIL_LINES = 80   # how much recent dialogue to show the model
    COVERAGE_BIAS = True         # flag already-explored options to nudge new branches

    # Ollama structured-output format. A JSON schema works on modern Ollama
    # (>= 0.5); set to the string "json" for older versions that lack schema
    # support (the prompt still asks for the same shape).
    _CHOICE_SCHEMA = {
        "type": "object",
        "properties": {
            "choice": {"type": "integer"},
            "reason": {"type": "string"},
        },
        "required": ["choice", "reason"],
    }
    OLLAMA_FORMAT = _CHOICE_SCHEMA

    SYSTEM_PROMPT = (
        "You are beta-testing a 1924 Scottish-manor murder-mystery visual novel. "
        "You read the dialogue so far and pick the choice a curious, in-character player "
        "would make to investigate the mystery. You are also testing branch coverage, so "
        "when two options seem equally sensible, prefer one that explores something new "
        "(options marked [already explored] have been seen on a previous visit). "
        "Reply ONLY with JSON of the form {\"choice\": <index>, \"reason\": <short reason>}. "
        "The index must be one of the numbers listed in CHOICES."
    )

    # ------------------------------------------------------------- prompt build
    def _transcript_tail():
        """Recent dialogue as plain 'Speaker: text' lines, sliced to the current scene."""
        try:
            lines = renpy.store._transcript_lines()
        except Exception:
            return ""
        # Focus on the current chapter: cut back to the last "Chapter:" marker.
        last_marker = -1
        for i, ln in enumerate(lines):
            if ln.startswith("Chapter:"):
                last_marker = i
        if last_marker >= 0:
            lines = lines[last_marker:]
        if len(lines) > TRANSCRIPT_TAIL_LINES:
            lines = lines[-TRANSCRIPT_TAIL_LINES:]
        return "\n".join(lines)

    def _choices_block(choices):
        rows = []
        for i, c in enumerate(choices):
            tag = ""
            if COVERAGE_BIAS and getattr(c, "already_chosen", False):
                tag = "   [already explored]"
            rows.append(u"{0}. {1}{2}".format(i, c.text, tag))
        return "\n".join(rows)

    def build_choice_prompt(transcript_tail, choices, stricter=False):
        user = (
            "STORY SO FAR:\n"
            + (transcript_tail or "(the scene has only just begun)")
            + "\n\nCHOICES (reply with the matching number):\n"
            + _choices_block(choices)
        )
        if stricter:
            user += "\n\nReturn STRICT JSON only, e.g. {\"choice\": 0, \"reason\": \"...\"}."
        return [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user},
        ]

    # ------------------------------------------------------------- ollama call
    def ollama_chat(messages, fmt=None, model=None, timeout=None):
        """POST a chat request to Ollama and return the assistant message content."""
        payload = {
            "model": model or OLLAMA_MODEL,
            "messages": messages,
            "stream": False,
            "options": {"temperature": TEMPERATURE},
        }
        if fmt is not None:
            payload["format"] = fmt
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            OLLAMA_URL,
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=timeout or OLLAMA_TIMEOUT) as resp:
            body = resp.read().decode("utf-8")
        obj = json.loads(body)
        return obj["message"]["content"]

    # ----------------------------------------------------------- decision log
    _decision_log = []

    def reset_decision_log():
        global _decision_log
        _decision_log = []

    def _log_decision(menu_id, choices, raw, idx, reason, note=""):
        chosen_text = None
        if idx is not None and 0 <= idx < len(choices):
            chosen_text = choices[idx].text
        _decision_log.append({
            "menu": menu_id,
            "choices": [c.text for c in choices],
            "chosen_index": idx,
            "chosen_text": chosen_text,
            "reason": reason,
            "raw_reply": raw,
            "note": note,
        })
        renpy.log("[OLLAMA] menu={0} -> idx={1} note={2} reason={3}".format(
            menu_id, idx, note, reason))

    def dump_decision_log():
        """Write this run's decisions next to the exported transcript, then clear."""
        global _decision_log
        if not _decision_log:
            return
        try:
            text_id = renpy.store.current_character.text_id
            chapter = renpy.store.current_chapter
            game_dir = renpy.config.gamedir

            chapters_order = list(renpy.store.chapters_names.keys())
            ci = chapters_order.index(chapter) if chapter in chapters_order else -1
            numbered = "{0}_{1}".format(ci, chapter) if ci >= 0 else str(chapter)

            out_dir = os.path.join(game_dir, "tests", "result", text_id, numbered)
            os.makedirs(out_dir, exist_ok=True)

            ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            fpath = os.path.join(out_dir, "ollama_decisions_{0}.json".format(ts))
            with open(fpath, "w", encoding="utf-8") as f:
                json.dump(_decision_log, f, indent=2, ensure_ascii=False)
        except Exception as e:
            renpy.log("[OLLAMA] failed to dump decision log: {0}".format(e))
        finally:
            _decision_log = []

    # ------------------------------------------------------------- the decision
    def decide_choice(timed_menu, valid_choices):
        """Return the index (into valid_choices) the LLM picks. Never raises on a
        model/network failure: it retries once, then falls back to the first valid
        choice and logs it loudly so the run completes and the failure is visible."""
        if not valid_choices:
            raise PlanError(
                "Ollama tester: no valid choices for menu '{0}'".format(timed_menu.id))
        if len(valid_choices) == 1:
            _log_decision(timed_menu.id, valid_choices, "", 0, "only valid option", "auto")
            return 0

        transcript = _transcript_tail()
        for attempt in range(2):
            try:
                raw = ollama_chat(
                    build_choice_prompt(transcript, valid_choices, stricter=(attempt > 0)),
                    fmt=OLLAMA_FORMAT,
                )
                parsed = json.loads(raw)
                idx = int(parsed.get("choice"))
                reason = str(parsed.get("reason", ""))
                if 0 <= idx < len(valid_choices):
                    _log_decision(timed_menu.id, valid_choices, raw, idx, reason)
                    return idx
                _log_decision(
                    timed_menu.id, valid_choices, raw, None, reason,
                    "index out of range" + (", retrying" if attempt == 0 else ""))
            except Exception as e:
                _log_decision(
                    timed_menu.id, valid_choices, "", None, "",
                    "ollama error: {0}".format(e) + (", retrying" if attempt == 0 else ""))

        _log_decision(
            timed_menu.id, valid_choices, "", 0,
            "fell back to first valid choice", "FALLBACK")
        return 0
