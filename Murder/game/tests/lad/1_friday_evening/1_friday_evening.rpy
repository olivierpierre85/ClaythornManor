testsuite lad_friday_evening:

    testcase lad_friday_evening_1:
        
        run Call("setup_lad_friday_evening_1")
        run Jump("lad_day1_evening")

        advance until screen "test_end"  timeout 180.0

        python:
            store.test.autorunner.reset()

    testcase lad_friday_evening_2:
        
        run Call("setup_lad_friday_evening_1")
        run Jump("lad_day1_evening")

        advance until screen "test_end"  timeout 180.0

        python:
            store.test.autorunner.reset()
