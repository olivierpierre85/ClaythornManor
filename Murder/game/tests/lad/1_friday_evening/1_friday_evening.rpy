testsuite lad_1_friday_evening_1:

    testcase lad_friday_evening:
        
        run Call("setup_lad_friday_evening_1")
        run Jump("lad_day1_evening")
        
        skip fast until label test_chapter_end timeout 180.0

        python:
            store.test.autorunner.reset()
            pass
