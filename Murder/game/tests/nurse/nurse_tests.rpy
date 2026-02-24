testsuite nurse:

    testcase friday_afternoon:
        python:
            test.start(nurse_details, "friday_afternoon", "tests/nurse/0_friday_afternoon/setup_nurse_friday_afternoon_1.json")
        run Jump("nurse_introduction")
        advance until screen "test_end" timeout 180.0
