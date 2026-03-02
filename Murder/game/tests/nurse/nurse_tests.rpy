testsuite nurse:

    testcase friday_afternoon:
        python:
            test.run_chapter(nurse_details, "friday_afternoon", "nurse_introduction")

    testcase friday_evening:
        python:
            test.run_chapter(nurse_details, 'friday_evening', 'nurse_day1_evening')

    testcase saturday_morning:
        python:
            test.run_chapter(nurse_details, 'saturday_morning', 'nurse_day2_morning')
