testsuite lad_friday_evening:

    testcase lad_friday_evening_1:
        
        python:
            test.start(lad_details, "friday_evening", "tests/lad/1_friday_evening/setup_lad_friday_evening_1.json")
        run Jump("lad_day1_evening")

        advance until screen "test_end"  timeout 180.0

        python:
            store.test.autorunner.reset()

    testcase lad_friday_evening_2:
        
        python:
            test.start(lad_details, "friday_evening", "tests/lad/1_friday_evening/setup_lad_friday_evening_1.json")
        run Jump("lad_day1_evening")

        advance until screen "test_end"  timeout 180.0

        python:
            store.test.autorunner.reset()
