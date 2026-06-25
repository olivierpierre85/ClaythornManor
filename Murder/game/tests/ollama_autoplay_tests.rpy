# Full-game autoplay launcher. Requires Ollama serving the model
# (see scripts/ollama_autoplay.rpy). Launch with:
#   renpy.exe  <project>  test ollama::autoplay
# Watch live in another terminal:
#   Get-Content -Wait game/tests/result/ollama_autoplay/session_*.log
testsuite ollama:

    testcase autoplay:
        python:
            test.run_autoplay(timeout=2000)
