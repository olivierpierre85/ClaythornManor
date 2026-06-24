testsuite captain:

    testcase friday_afternoon:
        python:
            test.run_chapter(captain_details, "friday_afternoon", "captain_introduction")

    testcase friday_evening:
        python:
            test.run_chapter(captain_details, "friday_evening", "captain_day1_evening")

    testcase saturday_morning:
        python:
            test.run_chapter(captain_details, "saturday_morning", "captain_day2_morning")

    testcase saturday_afternoon:
        python:
            test.run_chapter(captain_details, "saturday_afternoon", "captain_day2_hunt")

    testcase saturday_evening:
        python:
            test.run_chapter(captain_details, "saturday_evening", "captain_day2_evening")

    testcase sunday_morning:
        python:
            test.run_chapter(captain_details, "sunday_morning", "captain_day3_morning")

    testcase sunday_afternoon:
        python:
            test.run_chapter(captain_details, "sunday_afternoon", "captain_day3_afternoon")

    # --- Local-LLM (Ollama) beta tester: a local model picks every choice. ---
    # Requires Ollama serving the model (see tests/ollama_tester.rpy). Start small:
    #   renpy.exe  <project>  --test captain::ollama_friday_afternoon
    testcase ollama_friday_afternoon:
        python:
            test.run_chapter_ollama(captain_details, "friday_afternoon", "captain_introduction", runs=1)

    testcase ollama_friday_evening:
        python:
            test.run_chapter_ollama(captain_details, "friday_evening", "captain_day1_evening", runs=1)

    testcase ollama_saturday_morning:
        python:
            test.run_chapter_ollama(captain_details, "saturday_morning", "captain_day2_morning", runs=3)
