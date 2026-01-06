testsuite lad_0_friday_afternoon:

    testcase lad_friday_afternoon:
        run Call("setup_lad_friday_afternoon_1")
        run Jump("lad_introduction")

        # $ global current_chapter
        
        # Runs until your change_time detects the next chapter and jumps to __test_chapter_end
        # skip fast until label test_chapter_end timeout 180.0
        # advance until label test_chapter_end timeout 18000.0
        # advance until eval (current_chapter == "friday_evening") timeout 18000.0
        # advance until label lad_day1_evening

        advance until screen "test_end"
        # skip fast until screen "centered_text" timeout 180.0
        # skip fast until screen "centered_text" timeout 180.0
        

        python:
            # export_transcript(False)
            store.test.autorunner.reset()
