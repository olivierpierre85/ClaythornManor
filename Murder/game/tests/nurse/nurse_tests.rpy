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

    testcase saturday_afternoon:
        python:
            test.run_chapter(nurse_details, 'saturday_afternoon', 'nurse_day2_hunt')

    testcase saturday_evening:
        python:
            test.run_chapter(nurse_details, 'saturday_evening', 'nurse_day2_evening')

    testcase sunday_morning:
        python:
            test.run_chapter(nurse_details, 'sunday_morning', 'nurse_day3_morning')

    testcase sunday_afternoon:
        python:
            test.run_chapter(nurse_details, 'sunday_afternoon', 'nurse_day3_afternoon')