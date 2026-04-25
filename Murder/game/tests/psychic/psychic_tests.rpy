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
