testsuite broken:

    testcase friday_afternoon:
        python:
            test.run_chapter(broken_details, "friday_afternoon", "broken_introduction")

    testcase friday_evening:
        python:
            test.run_chapter(broken_details, "friday_evening", "broken_day1_evening")

    testcase saturday_afternoon:
        python:
            test.run_chapter(broken_details, "saturday_afternoon", "broken_day2_hunt")

    testcase saturday_evening:
        python:
            test.run_chapter(broken_details, "saturday_evening", "broken_day2_evening")

    testcase sunday_morning:
        python:
            test.run_chapter(broken_details, "sunday_morning", "broken_day3_morning")

    testcase sunday_afternoon:
        python:
            test.run_chapter(broken_details, "sunday_afternoon", "broken_day3_afternoon")
