# Local-LLM (Ollama) testing - a model picks every choice. Still in
# development, so the whole suite is disabled in the default test run
# (`enabled False`). It only runs when named explicitly:
#   renpy.exe  <project>  test ollama
#   renpy.exe  <project>  test ollama::captain_friday_evening
#   renpy.exe  <project>  test ollama::autoplay
# Requires Ollama serving the model first (see tests/ollama_tester.rpy and
# scripts/ollama_autoplay.rpy). Watch the autoplay live in another terminal:
#   Get-Content -Wait game/tests/result/ollama_autoplay/session_*.log
testsuite ollama:
    enabled False

    # --- Per-chapter beta tester: the model plays one chapter. Start small. ---
    testcase captain_friday_afternoon:
        python:
            test.run_chapter_ollama(captain_details, "friday_afternoon", "captain_introduction", runs=1)

    testcase captain_friday_evening:
        python:
            test.run_chapter_ollama(captain_details, "friday_evening", "captain_day1_evening", runs=1)

    testcase captain_saturday_morning:
        python:
            test.run_chapter_ollama(captain_details, "saturday_morning", "captain_day2_morning", runs=3)

    # --- Full-game autoplay: the model plays until every ending is reached. ---
    testcase autoplay:
        python:
            test.run_autoplay(timeout=2000)
