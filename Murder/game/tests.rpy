testsuite global:
    setup:
        pause until screen "main_menu" timeout 20.0

    before testsuite:
        pause until screen "main_menu" timeout 20.0
        run Start()

    teardown:
        exit

    testsuite lad_friday_evening:

        testcase lad_day1_evening_pathA:

            python:
                test.autorunner.reset()
                # test.autorunner.load_plan_file("testing_paths/lad/1_friday_evening/choices_anon_2025-10-01_11-00-29.json")
                test.autorunner.load_plan_file("choices_anon_2025-10-01_11-00-29.json")

                # Manual previous-chapter threads for this test
                test.unlock_threads(lad_details, [
                    "whisky",
                    # "day1_drunk",
                ])

                # If your story uses these globals, set them as needed:
                store.current_character = lad_details

            run Jump("lad_day1_evening")

            # Runs until your change_time detects the next chapter and jumps to __test_chapter_end
            skip fast until label __test_chapter_end timeout 180.0

            python:
                test.autorunner.assert_consumed()
                test.autorunner.reset()
