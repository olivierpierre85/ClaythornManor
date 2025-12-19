testsuite global:
    setup:
        pause until screen "main_menu" timeout 20.0

    before testsuite:
        pause until screen "main_menu" timeout 20.0
        run Start()

    teardown:
        exit

    testsuite lad_friday_evening:

        testcase lad_day1_afternoon_pathA:

            python:
                store.test.autorunner.reset()
                # store.test.autorunner.load_plan_file("testing_paths/lad/1_friday_evening/choices_anon_2025-10-01_11-00-29.json")
                store.test.autorunner.load_plan_file("choices_anon_2025-10-01_11-00-29.json")

                # Manual previous-chapter threads for this test
                store.test.unlock_threads(lad_details, [
                    "whisky",
                    # "day1_drunk",
                ])

                # If your story uses these globals, set them as needed:
                store.current_character = lad_details

                store.test.autorunner.target_chapter = "friday_afternoon"

            run Jump("lad_introduction")

            # Runs until your change_time detects the next chapter and jumps to __test_chapter_end
            skip fast until label test_chapter_end timeout 180.0

            python:
                # store.test.autorunner.assert_consumed() # Cannot assert consumed on partial run
                store.test.autorunner.reset()
