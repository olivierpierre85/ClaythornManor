testsuite drunk:

    testcase friday_afternoon:
        python:
            test.run_chapter(drunk_details, "friday_afternoon", "drunk_introduction")

    testcase friday_evening:
        python:
            test.run_chapter(drunk_details, "friday_evening", "drunk_day1_evening")

    testcase saturday_morning:
        python:
            test.run_chapter(drunk_details, "saturday_morning", "drunk_day2_morning")

    testcase saturday_afternoon:
        python:
            test.run_chapter(drunk_details, "saturday_afternoon", "drunk_day2_hunt")

    testcase saturday_evening:
        python:
            test.run_chapter(drunk_details, "saturday_evening", "drunk_day2_evening")

    testcase sunday_morning:
        python:
            test.run_chapter(drunk_details, "sunday_morning", "drunk_day3_morning")

    testcase sunday_afternoon:
        python:
            test.run_chapter(drunk_details, "sunday_afternoon", "drunk_day3_afternoon")
