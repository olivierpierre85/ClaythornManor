testsuite global:
    setup:
        pause until screen "main_menu" timeout 20.0

    before testsuite:
        pause until screen "main_menu" timeout 20.0
        run Start()

    teardown:
        exit

    testsuite lad_friday_evening:

        testcase lad_day1_afternoon_pathA:

            run Call("setup_test_lad_friday")

            run Jump("lad_introduction")

            # Runs until your change_time detects the next chapter and jumps to __test_chapter_end
            skip fast until label test_chapter_end timeout 180.0

            python:
                # store.test.autorunner.assert_consumed() # Cannot assert consumed on partial run
                store.test.autorunner.reset()
