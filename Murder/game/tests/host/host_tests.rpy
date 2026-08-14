testsuite host:

    testcase friday_afternoon:
        python:
            test.run_chapter(host_details, "friday_afternoon", "host_introduction")

    testcase friday_evening:
        python:
            test.run_chapter(host_details, "friday_evening", "host_day1_evening")

    testcase saturday_morning:
        python:
            test.run_chapter(host_details, "saturday_morning", "host_day2_morning")
