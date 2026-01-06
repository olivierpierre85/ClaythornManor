testsuite lad_friday_afternoon:

    testcase lad_friday_afternoon_1:
        run Call("setup_lad_friday_afternoon_1")
        run Jump("lad_introduction")

        advance until screen "test_end" timeout 180.0

        python:
            store.test.autorunner.reset()
