testsuite lad:

    testcase friday_afternoon:
        python:
            test.run_chapter(lad_details, "friday_afternoon", "lad_introduction")

    testcase friday_evening:
        python:
            test.run_chapter(lad_details, "friday_evening", "lad_day1_evening")

    testcase saturday_morning:
        python:
            test.run_chapter(lad_details, "saturday_morning", "lad_day2_morning")

    testcase saturday_afternoon_no_hunt:
        python:
            test.run_chapter(lad_details, "saturday_afternoon_no_hunt", "lad_day2_no_hunt")

    testcase saturday_afternoon:
        python:
            test.run_chapter(lad_details, "saturday_afternoon", "lad_day2_hunt")

    testcase saturday_evening:
        python:
            test.run_chapter(lad_details, "saturday_evening", "lad_day2_evening")

    testcase sunday_morning:
        python:
            test.run_chapter(lad_details, "sunday_morning", "lad_day3_morning")

    testcase sunday_afternoon:
        python:
            test.run_chapter(lad_details, "sunday_afternoon", "lad_day3_afternoon")
