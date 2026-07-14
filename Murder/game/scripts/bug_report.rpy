# Tester bug-report system.
#
# Sends crash reports and manual tester feedback to a Discord webhook, with a
# local export (desktop) or browser download (web) as fallback. The crash path
# is wired in dump_state (script.rpy); the feedback path is the "Report"
# overlay button below. The attached report JSON keeps the same top-level
# "choices" key as the manual exports so it can be replayed by the test runner.

define BUG_REPORT_ENABLED = True

# Discord channel webhook URL (Channel settings -> Integrations -> Webhooks).
# Reports arrive as messages with the full report JSON attached as a file.
define BUG_REPORT_WEBHOOK_URL = "https://discord.com/api/webhooks/1522533798204411945/JWh51TRDQjngObMxxtYSGrOy5O-a95_KUycG78vjDOzIywbpnyeT_ArWp7NjtNnAADGk"

default persistent.tester_id = None
default bug_report_text = ""

init python:
    # NEVER import datetime or time here (script.rpy binds the classes)
    import urllib.request
    import ssl
    import traceback as _traceback_module

    # Ren'Py's bundled Python has no CA certificates wired into urllib, so
    # HTTPS fails with CERTIFICATE_VERIFY_FAILED without this context.
    try:
        import certifi
        _bug_report_ssl_context = ssl.create_default_context(cafile=certifi.where())
    except Exception:
        _bug_report_ssl_context = None

    def _log_bug_report_error():
        # Last-resort diagnostics: append the traceback to a log file so a
        # failed send is never a silent mystery.
        try:
            out_dir = os.path.join(renpy.config.gamedir, "tests", "bug_reports")
            os.makedirs(out_dir, exist_ok=True)
            with open(os.path.join(out_dir, "send_errors.log"), "a", encoding="utf-8") as f:
                f.write("---- {} ----\n{}\n".format(
                    datetime.now().isoformat(), _traceback_module.format_exc()))
        except Exception:
            pass

    def _bug_report_context():
        context = {}
        try:
            character = getattr(renpy.store, "current_character", None)
            chapter = getattr(renpy.store, "current_chapter", None)
            chapter_names = getattr(renpy.store, "chapters_names", None) or {}
            context = {
                "character": getattr(character, "text_id", None),
                "character_name": getattr(character, "real_name", None),
                "chapter": chapter,
                "chapter_name": chapter_names.get(chapter),
                "room": getattr(renpy.store, "current_room", None),
                "time_left": getattr(renpy.store, "time_left", None),
                "position": getattr(renpy.store, "current_position", None),
                "run": getattr(renpy.store, "current_run", None),
            }
        except Exception:
            pass
        return context

    def build_bug_report(report_type, message=None, short_tb=None, full_tb=None):
        tester = str(persistent.tester_id or "anonymous")
        platform_name = "web" if sys.platform == "emscripten" else "pc"
        context = _bug_report_context()

        report = {
            "type": report_type,
            "tester_id": tester,
            "timestamp": datetime.now().isoformat(),
            "version": config.version,
            "platform": platform_name,
            "context": context,
            "message": message,
            "short_tb": short_tb,
            "full_tb": full_tb,
            # Same top-level keys as export_choices_to_file, so the attachment
            # can be dropped into tests/testing_mode_choices/ and replayed.
            "unlocked_threads": [],
            "choices": getattr(renpy.store, "all_choices", []),
        }
        report_json_str = json.dumps(report, indent=2, ensure_ascii=False, default=str)

        details = short_tb if report_type == "crash" else message
        content = (
            "**{}** - {} v{} - tester: {}\n"
            "char: {} | chapter: {} | room: {} | time_left: {} | platform: {}\n"
            "```\n{}\n```"
        ).format(
            report_type.upper(), config.name, config.version, tester,
            context.get("character"), context.get("chapter"), context.get("room"),
            context.get("time_left"), platform_name,
            (details or "").strip()[:1500],
        )
        # Discord hard limits: content 2000 chars, username 80 chars.
        payload_json_str = json.dumps(
            {"username": tester[:32], "content": content[:1900]},
            ensure_ascii=False)

        ts = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = "report_{}_{}_{}.json".format(report_type, _sanitize(tester), ts)

        return payload_json_str, report_json_str, file_name

    def _send_report_desktop(payload_json_str, report_json_str, file_name, timeout=10):
        boundary = "----ClaythornBugReport" + uuid.uuid4().hex
        body = (
            "--{b}\r\n"
            "Content-Disposition: form-data; name=\"payload_json\"\r\n"
            "Content-Type: application/json\r\n\r\n"
            "{pj}\r\n"
            "--{b}\r\n"
            "Content-Disposition: form-data; name=\"files[0]\"; filename=\"{fn}\"\r\n"
            "Content-Type: application/json\r\n\r\n"
        ).format(b=boundary, pj=payload_json_str, fn=file_name).encode("utf-8")
        body += report_json_str.encode("utf-8")
        body += "\r\n--{}--\r\n".format(boundary).encode("utf-8")

        req = urllib.request.Request(
            BUG_REPORT_WEBHOOK_URL,
            data=body,
            headers={
                "Content-Type": "multipart/form-data; boundary=" + boundary,
                "User-Agent": "ClaythornManor/" + config.version,
            },
            method="POST")

        with urllib.request.urlopen(req, timeout=timeout, context=_bug_report_ssl_context) as resp:
            return 200 <= resp.status < 300

    def _send_report_web(payload_json_str, report_json_str, file_name):
        # Fire-and-forget browser fetch, independent of the Python interaction
        # state (safe at crash time). Payloads travel as base64 so we never
        # worry about quoting. On failure the catch handler downloads the
        # report file instead, like export_choices_to_file does.
        pj_b64 = base64.b64encode(payload_json_str.encode("utf-8")).decode("ascii")
        file_b64 = base64.b64encode(report_json_str.encode("utf-8")).decode("ascii")

        js = """
            (function () {{
                function b64ToBytes(b64) {{
                    var bin = atob(b64);
                    var bytes = new Uint8Array(bin.length);
                    for (var i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
                    return bytes;
                }}
                var fileBytes = b64ToBytes("{file_b64}");
                var fd = new FormData();
                fd.append("payload_json", new TextDecoder("utf-8").decode(b64ToBytes("{pj_b64}")));
                fd.append("files[0]", new Blob([fileBytes], {{ type: "application/json" }}), "{fn}");
                fetch("{url}", {{ method: "POST", body: fd }})
                    .then(function (r) {{ console.log("bug report:", r.status); }})
                    .catch(function (e) {{
                        console.log("bug report failed, downloading instead", e);
                        var a = document.createElement('a');
                        a.href = URL.createObjectURL(new Blob([fileBytes], {{ type: 'application/json' }}));
                        a.download = "{fn}";
                        document.body.appendChild(a);
                        a.click();
                        document.body.removeChild(a);
                    }});
            }})();
        """.format(file_b64=file_b64, pj_b64=pj_b64, fn=file_name, url=BUG_REPORT_WEBHOOK_URL)

        renpy.emscripten.run_script(js)
        return True

    def send_bug_report(report_type, message=None, short_tb=None, full_tb=None):
        if not BUG_REPORT_ENABLED or not BUG_REPORT_WEBHOOK_URL or "XXXX" in BUG_REPORT_WEBHOOK_URL:
            return False
        try:
            payload_json_str, report_json_str, file_name = build_bug_report(
                report_type, message=message, short_tb=short_tb, full_tb=full_tb)
            if sys.platform == "emscripten":
                return _send_report_web(payload_json_str, report_json_str, file_name)
            return _send_report_desktop(payload_json_str, report_json_str, file_name)
        except Exception:
            _log_bug_report_error()
            return False

    def _save_report_locally(report_json_str, file_name):
        try:
            out_dir = os.path.join(renpy.config.gamedir, "tests", "bug_reports")
            os.makedirs(out_dir, exist_ok=True)
            with open(os.path.join(out_dir, file_name), "w", encoding="utf-8") as f:
                f.write(report_json_str)
            return True
        except Exception:
            return False

    def open_bug_report_modal():
        store.bug_report_text = ""
        if not persistent.tester_id:
            persistent.tester_id = ""
        renpy.show_screen("bug_report_modal")
        renpy.restart_interaction()

    def submit_feedback_report():
        message = (bug_report_text or "").strip()
        if not message:
            renpy.notify("Please enter a message first.")
            return
        renpy.hide_screen("bug_report_modal")
        if send_bug_report("feedback", message=message):
            renpy.notify("Report sent - thank you!")
        else:
            saved = False
            if sys.platform != "emscripten":
                try:
                    _pj, report_json_str, file_name = build_bug_report("feedback", message=message)
                    saved = _save_report_locally(report_json_str, file_name)
                except Exception:
                    saved = False
            if saved:
                renpy.notify("Could not send - saved locally instead.")
            else:
                renpy.notify("Could not send the report.")
        store.bug_report_text = ""
        renpy.restart_interaction()

screen bug_report_button:
    if BUG_REPORT_ENABLED and not renpy.get_screen("bug_report_modal") and not renpy.get_screen("input") and not overlay_ui_hidden():
        modal False
        zorder 1000
        style_prefix "confirm"  # TODO use own style
        # Below the Menu button: the top-left corner is taken by the clock
        frame:
            xalign 1.0
            yalign 0.0
            xoffset -30
            yoffset 130
            ypadding 0
            xpadding 0
            textbutton _("Report BUG"):
                action Function(open_bug_report_modal)
                xminimum 200
                yminimum 80
                text_size 18

screen bug_report_modal:
    modal True
    zorder 1100
    style_prefix "confirm"  # TODO use own style

    default name_value = FieldInputValue(persistent, "tester_id", default=False)
    default message_value = VariableInputValue("bug_report_text", default=True)

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 40

        vbox:
            spacing 20

            label _("Report a problem or send feedback")

            hbox:
                spacing 10
                text _("Name:") yalign 0.5
                button:
                    key_events True
                    action name_value.Enable()
                    input value name_value length 32 copypaste True

            frame:
                xsize 900
                ysize 300
                button:
                    key_events True
                    xfill True
                    yfill True
                    action message_value.Enable()
                    input value message_value multiline True length 1500 copypaste True xmaximum 860 align (0.0, 0.0)

            hbox:
                spacing 40
                xalign 0.5
                textbutton _("Send") action Function(submit_feedback_report)
                textbutton _("Cancel") action Hide("bug_report_modal")

init python:
    config.overlay_screens.append("bug_report_button")
