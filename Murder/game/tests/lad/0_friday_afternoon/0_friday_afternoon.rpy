testsuite lad_friday_afternoon:

    testcase lad_friday_afternoon_1:
        python:
            test.start(lad_details, "friday_afternoon", "tests/lad/1_friday_evening/setup_lad_friday_evening_1.json")
        run Jump("lad_introduction")

        advance until screen "test_end" timeout 180.0

        python:
            store.test.autorunner.reset()
