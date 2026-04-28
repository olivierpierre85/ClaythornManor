testsuite psychic:

    testcase friday_afternoon:
        python:
            test.run_chapter(psychic_details, "friday_afternoon", "psychic_introduction")

    testcase friday_evening:
        python:
            test.run_chapter(psychic_details, "friday_evening", "psychic_day1_evening")

    testcase saturday_morning:
        python:
            test.run_chapter(psychic_details, "saturday_morning", "psychic_day2_morning")

    testcase saturday_afternoon:
        python:
            test.run_chapter(psychic_details, "saturday_afternoon", "psychic_day2_no_hunt")

    testcase saturday_evening:
        python:
            test.run_chapter(psychic_details, "saturday_evening", "psychic_day2_evening")

    testcase sunday_morning:
        python:
            test.run_chapter(psychic_details, "sunday_morning", "psychic_day3_morning")

    testcase sunday_afternoon:
        python:
            test.run_chapter(psychic_details, "sunday_afternoon", "psychic_day3_afternoon")
