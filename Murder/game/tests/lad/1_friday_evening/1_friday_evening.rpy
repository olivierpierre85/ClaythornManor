testsuite lad_1_friday_evening_1:

    testcase lad_friday_evening:
        
        run Call("setup_lad_friday_evening_1")
        run Jump("lad_day1_evening")
        
        # skip fast until label test_chapter_end timeout 180.0
        # skip until label test_chapter_end 

        skip until label lad_day2_morning timeout 180.0
        # advance until menu choice

        python:
            # test_teardown()
            export_transcript(False)
            pass
