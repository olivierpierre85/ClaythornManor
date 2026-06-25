# Full-game cross-character autoplay tester driven by a local LLM (Ollama).
#
# A master switch `ollama_autoplay` reroutes the game's three decision points to the
# model so it plays like a real player from lad_introduction onward:
#   - menus / maps      -> ollama_pick_menu_choice()      (hooked in display_choices)
#   - character select  -> ollama_pick_character()        (hooked in character_selection)
#   - death / escape / work_in_progress -> ollama_autoplay_checkpoint (continue or stop)
#
# It is launched through the Ren'Py test runner purely to boot past the main menu and
# auto-advance dialogue (see tests/ollama_autoplay_tests.rpy -> `test ollama::autoplay`).
# Every decision is appended (and flushed) to a live session log you can tail:
#   game/tests/result/ollama_autoplay/session_<ts>.log   (human readable)
#   game/tests/result/ollama_autoplay/session_<ts>.jsonl (structured)
#
# Off by default: zero effect on normal play or the existing chapter tests.

default ollama_autoplay = False

# Session counters / paths kept in one dict so saving stays picklable (no file handles).
default _ollama_state = {}

init python:
    # NOTE: `datetime`, `time`, `date`, `os`, `json` are already bound in the store by
    # script.rpy's `from datetime import datetime, time, ...` (so `datetime` here is the
    # datetime CLASS, not the module). Do NOT `import datetime`/`import time` - that
    # would shadow those globals and break the game's clock code. We only need urllib.
    import urllib.request
    import random as _rng

    # ---------------------------------------------------------------- config
    # Confirm the model tag with `ollama list`.
    OLLAMA_URL = "http://localhost:11434/api/chat"
    OLLAMA_MODEL = "gemma4:12b-it-qat"
    OLLAMA_TIMEOUT = 120          # per request, seconds (12B can need >30s on big prompts)
    OLLAMA_TEMPERATURE = 0.6
    OLLAMA_TRANSCRIPT_TAIL = 60  # lines of recent dialogue shown to the model

    # Safety cap (the practical terminator until the real game ending exists).
    OLLAMA_MAX_DECISIONS = 600
    OLLAMA_MAX_SECONDS = 1800
    OLLAMA_STALL_RUNS = 12       # stop after this many endings with no new ending reached

    _OLLAMA_CHOICE_SCHEMA = {
        "type": "object",
        "properties": {
            "choice": {"type": "integer"},
            "reason": {"type": "string"},
        },
        "required": ["choice", "reason"],
    }

    OLLAMA_SYSTEM_MENU = (
        "You are beta-testing a 1924 Scottish-manor murder-mystery visual novel. "
        "Read the dialogue so far and pick the option a curious, in-character player would "
        "choose to investigate the mystery. You are testing coverage, so when options seem "
        "equally good, prefer exploring something new. "
        "Reply ONLY as JSON {\"choice\": <index>, \"reason\": <short reason>}. "
        "The index must be one of the numbers listed."
    )
    OLLAMA_SYSTEM_CHARACTER = (
        "You are beta-testing this murder-mystery visual novel by playing through every "
        "character's storyline. Choose which character to play next. Prefer characters who "
        "still have unreached endings so the whole game gets covered. "
        "Reply ONLY as JSON {\"choice\": <index>, \"reason\": <short reason>}. "
        "The index must be one of the numbers listed."
    )

    # ------------------------------------------------------------ ollama call
    def ollama_chat(messages, fmt=None):
        payload = {
            "model": OLLAMA_MODEL,
            "messages": messages,
            "stream": False,
            "options": {"temperature": OLLAMA_TEMPERATURE},
        }
        if fmt is not None:
            payload["format"] = fmt
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            OLLAMA_URL, data=data,
            headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=OLLAMA_TIMEOUT) as resp:
            body = resp.read().decode("utf-8")
        return json.loads(body)["message"]["content"]

    def ollama_transcript_tail(n=None):
        if n is None:
            n = OLLAMA_TRANSCRIPT_TAIL
        try:
            lines = renpy.store._transcript_lines()
        except Exception:
            return ""
        last_marker = -1
        for i, ln in enumerate(lines):
            if ln.startswith("Chapter:"):
                last_marker = i
        if last_marker >= 0:
            lines = lines[last_marker:]
        if len(lines) > n:
            lines = lines[-n:]
        return "\n".join(lines)

    def ollama_choose(system_prompt, transcript, options):
        """Ask the model to pick one of `options` (list of strings).
        Returns (index, reason, raw_reply, note). Never raises: retries once then
        falls back to index 0 with note='FALLBACK'."""
        base = (
            "STORY SO FAR:\n" + (transcript or "(the scene has only just begun)")
            + "\n\nOPTIONS (reply with the matching number):\n"
            + "\n".join(u"{0}. {1}".format(i, o) for i, o in enumerate(options))
        )
        for attempt in range(2):
            try:
                user = base + ("\n\nReturn STRICT JSON {\"choice\": <int>, \"reason\": <str>}." if attempt else "")
                raw = ollama_chat(
                    [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user},
                    ],
                    _OLLAMA_CHOICE_SCHEMA)
                parsed = json.loads(raw)
                idx = int(parsed.get("choice"))
                reason = str(parsed.get("reason", ""))
                if 0 <= idx < len(options):
                    return idx, reason, raw, ""
            except Exception as e:
                renpy.log("[ollama] choose error (attempt {0}): {1}".format(attempt, e))
        # Last resort: a random valid option, so repeated fallbacks don't hammer index 0.
        return _rng.randrange(len(options)), "", "", "FALLBACK"

    # ----------------------------------------------------------- session log
    def _ollama_now():
        return datetime.now().strftime("%H:%M:%S")

    def _ollama_write(path_key, text):
        path = _ollama_state.get(path_key)
        if not path:
            return
        try:
            with open(path, "a", encoding="utf-8") as f:
                f.write(text + "\n")
        except Exception as e:
            renpy.log("[ollama] log write failed: {0}".format(e))

    def ollama_session_open():
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_dir = os.path.join(renpy.config.gamedir, "tests", "result", "ollama_autoplay")
        try:
            os.makedirs(out_dir, exist_ok=True)
        except Exception as e:
            renpy.log("[ollama] mkdir failed: {0}".format(e))
        _ollama_state.clear()
        _ollama_state["log"] = os.path.join(out_dir, "session_{0}.log".format(ts))
        _ollama_state["jsonl"] = os.path.join(out_dir, "session_{0}.jsonl".format(ts))
        _ollama_state["count"] = 0
        _ollama_state["stall"] = 0
        _ollama_state["endings_seen"] = ollama_total_unlocked_endings()
        _ollama_state["start"] = datetime.now()
        _ollama_write("log", "=== Ollama autoplay session {0} (model {1}) ===".format(ts, OLLAMA_MODEL))

    def ollama_log_decision(kind, char_id, options, idx, reason, note, menu_id=None, level=None):
        _ollama_state["count"] = _ollama_state.get("count", 0) + 1
        chosen = options[idx] if (0 <= idx < len(options)) else "?"
        chosen_short = chosen if len(chosen) <= 80 else chosen[:77] + "..."
        flag = (" [" + note + "]") if note else ""
        # Show menu id + nesting level so parent hubs vs. conversation sub-menus (and
        # scene transitions) are visible in the log rather than ambiguous.
        ctx = kind
        if menu_id is not None:
            ctx = u"{0}(L{1} {2})".format(kind, level if level is not None else "?", menu_id)
        _ollama_write("log", u"[{0}] {1} char={2}{3} -> #{4} '{5}'  | reason: {6}".format(
            _ollama_now(), ctx, char_id, flag, idx, chosen_short, reason))
        _ollama_write("jsonl", json.dumps({
            "t": datetime.now().isoformat(),
            "kind": kind, "menu": menu_id, "level": level,
            "char": char_id, "options": options,
            "chosen_index": idx, "chosen": chosen, "reason": reason, "note": note,
            "decision": _ollama_state.get("count"),
        }, ensure_ascii=False))

    # ----------------------------------------------------------- the choosers
    def _ollama_current_char_id():
        cur = getattr(renpy.store, "current_character", None)
        return getattr(cur, "text_id", "?") if cur else "?"

    def ollama_pick_menu_choice(timed_menu):
        # Autoplay resolves a menu with a silent Python call (no call_screen
        # interaction), so a fast-re-displaying menu can execute 100+ statements per
        # second and trip Ren'Py's infinite-loop guard (execution.py). Reset that timer
        # each decision; a *genuine* soft-lock is still caught by the repeat guard below.
        renpy.not_infinite_loop(30)

        if getattr(timed_menu, "is_map", False):
            valid = [c for c in timed_menu.choices if c.get_condition()]
            kind = "MAP"
        else:
            valid = [c for c in timed_menu.choices if c.is_valid()]
            kind = "MENU"
        if not valid:
            # Should not happen (display_choices only calls us for a shown menu).
            return timed_menu.choices[0]
        options = [c.text for c in valid]
        mid = getattr(timed_menu, "id", None)
        level = getattr(renpy.store, "menu_level", None)

        # Soft-lock guard: a normal conversation sub-menu re-displays only a handful of
        # times (once per topic). If the SAME menu keeps re-appearing far beyond that,
        # force an exit so the run continues and flag it as a potential soft-lock.
        if _ollama_state.get("last_menu") == mid:
            _ollama_state["menu_repeat"] = _ollama_state.get("menu_repeat", 0) + 1
        else:
            _ollama_state["last_menu"] = mid
            _ollama_state["menu_repeat"] = 0

        if _ollama_state.get("menu_repeat", 0) >= 40:
            exits = [c for c in valid if getattr(c, "early_exit", False)]
            target = exits[0] if exits else valid[-1]
            ti = valid.index(target)
            ollama_log_decision(
                kind, _ollama_current_char_id(), options, ti,
                "menu re-displayed 40+ times in a row; forcing exit", "SOFTLOCK?",
                menu_id=mid, level=level)
            _ollama_state["menu_repeat"] = 0
            return target

        if len(valid) == 1:
            idx, reason, note = 0, "only valid option", "auto"
        else:
            idx, reason, _raw, note = ollama_choose(OLLAMA_SYSTEM_MENU, ollama_transcript_tail(), options)
        ollama_log_decision(
            kind, _ollama_current_char_id(), options, idx, reason, note,
            menu_id=mid, level=level)
        return valid[idx]

    def _ollama_missing_endings(char):
        e = getattr(char, "endings", None)
        if not e:
            return [], 0
        items = list(e)
        missing = [it.text_id for it in items if getattr(it, "locked", False)]
        return missing, len(items)

    def ollama_pick_character():
        flat = getattr(renpy.store, "char_list_flat", [])
        unlocked = [c for c in flat if c.is_character_unlocked()]
        if not unlocked:
            return "lad"
        options = []
        for c in unlocked:
            missing, total = _ollama_missing_endings(c)
            reached = total - len(missing)
            options.append(u"{0} ({1}) - {2}/{3} endings reached; still missing: {4}".format(
                c.real_name, c.text_id, reached, total, ", ".join(missing) if missing else "none"))
        idx, reason, _raw, note = ollama_choose(OLLAMA_SYSTEM_CHARACTER, ollama_transcript_tail(20), options)
        ollama_log_decision("CHARACTER_SELECT", _ollama_current_char_id(), options, idx, reason, note,
                            menu_id="character_selection", level=0)
        return unlocked[idx].text_id

    # ------------------------------------------------------ endings / termination
    def ollama_total_unlocked_endings():
        total = 0
        for c in getattr(renpy.store, "char_list_flat", []):
            e = getattr(c, "endings", None)
            if e:
                total += len(e.get_unlocked())
        return total

    def ollama_total_all_endings():
        total = 0
        for c in getattr(renpy.store, "char_list_flat", []):
            e = getattr(c, "endings", None)
            if e:
                total += len(list(e))
        return total

    def all_endings_reached():
        for c in getattr(renpy.store, "char_list_flat", []):
            e = getattr(c, "endings", None)
            if not e:
                continue
            if len(e.get_unlocked()) < len(list(e)):
                return False
        return True

    def ollama_note_ending(kind):
        now_total = ollama_total_unlocked_endings()
        if now_total > _ollama_state.get("endings_seen", 0):
            _ollama_state["endings_seen"] = now_total
            _ollama_state["stall"] = 0
        else:
            _ollama_state["stall"] = _ollama_state.get("stall", 0) + 1
        _ollama_write("log", "[ENDING] kind={0} char={1} endings={2}/{3} stall={4} decisions={5}".format(
            kind, _ollama_current_char_id(), now_total, ollama_total_all_endings(),
            _ollama_state.get("stall"), _ollama_state.get("count")))

    def ollama_autoplay_should_stop():
        if all_endings_reached():
            return "all endings reached"
        if _ollama_state.get("count", 0) >= OLLAMA_MAX_DECISIONS:
            return "decision cap"
        _start = _ollama_state.get("start")
        if _start and (datetime.now() - _start).total_seconds() >= OLLAMA_MAX_SECONDS:
            return "time cap"
        if _ollama_state.get("stall", 0) >= OLLAMA_STALL_RUNS:
            return "stalled (no new ending)"
        return None

    def ollama_finalize_session(reason):
        try:
            export_transcript(True)
        except Exception as e:
            renpy.log("[ollama] final transcript failed: {0}".format(e))
        _start = _ollama_state.get("start")
        elapsed = (datetime.now() - _start).total_seconds() if _start else 0
        _ollama_write("log", "=== SESSION END ({0}): decisions={1} endings={2}/{3} elapsed={4:.0f}s ===".format(
            reason, _ollama_state.get("count"), ollama_total_unlocked_endings(),
            ollama_total_all_endings(), elapsed))


# --- Entry point: start a full autoplay session from the very beginning ---
label start_ollama_autoplay:

    $ ollama_autoplay = True
    $ config.autosave_on_choice = False

    call init_debug

    # Timing is left faithful on purpose: init_debug sets infinite_time_activated = False,
    # so the per-menu time budgets apply just like a real player (conversations are
    # time-boxed, and the story advances toward endings). To let the model exhaust every
    # conversation branch instead, set `infinite_time_activated = True` AFTER this call.

    $ ollama_session_open()

    $ current_character = lad_details
    $ current_storyline = lad_details

    jump lad_introduction


# --- Called at every death / escape / work_in_progress while autoplaying ---
label ollama_autoplay_checkpoint(kind="ending"):

    $ ollama_note_ending(kind)

    python:
        _ollama_stop_reason = ollama_autoplay_should_stop()

    if _ollama_stop_reason:
        $ ollama_finalize_session(_ollama_stop_reason)
        $ renpy.show_screen("test_end")
        jump test_end_pause

    return
