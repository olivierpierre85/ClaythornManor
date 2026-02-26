testsuite nurse:

    testcase friday_afternoon:
        python:
            test.start(nurse_details, "friday_afternoon", "tests/nurse/0_friday_afternoon/setup_nurse_friday_afternoon_1.json")
        run Jump("nurse_introduction")
        advance until screen "test_end" timeout 180.0

    testcase friday_evening:
        python:
            test_plan_runner.run_chapter(nurse_details, 'friday_evening', 'nurse_day1_evening')
