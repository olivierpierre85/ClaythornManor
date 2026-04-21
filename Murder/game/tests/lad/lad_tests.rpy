testsuite lad:

    testcase friday_afternoon:
        python:
            test.run_chapter(lad_details, "friday_afternoon", "lad_introduction")

    testcase friday_evening:
        python:
            test.run_chapter(lad_details, "friday_evening", "lad_day1_evening")

    testcase saturday_afternoon_no_hunt:
        python:
            test.run_chapter(lad_details, "saturday_afternoon_no_hunt", "lad_day2_no_hunt")
