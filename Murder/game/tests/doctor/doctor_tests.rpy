testsuite doctor:

    testcase friday_afternoon:
        python:
            test.run_chapter(doctor_details, "friday_afternoon", "doctor_introduction")

    testcase friday_evening:
        python:
            test.run_chapter(doctor_details, "friday_evening", "doctor_day1_evening")

    testcase saturday_morning:
        python:
            test.run_chapter(doctor_details, "saturday_morning", "doctor_day2_morning")

    testcase saturday_afternoon:
        python:
            test.run_chapter(doctor_details, "saturday_afternoon", "doctor_day2_hunt")

    testcase saturday_evening:
        python:
            test.run_chapter(doctor_details, "saturday_evening", "doctor_day2_evening")

    testcase sunday_morning:
        python:
            test.run_chapter(doctor_details, "sunday_morning", "doctor_day3_morning")

    testcase sunday_afternoon:
        python:
            test.run_chapter(doctor_details, "sunday_afternoon", "doctor_day3_afternoon")
