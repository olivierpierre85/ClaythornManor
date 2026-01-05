# testsuite lad_0_friday_afternoon:


#     testcase lad_friday_afternoon:
#         run Call("setup_test_lad_friday")
#         run Jump("lad_introduction")
        
#         # Runs until your change_time detects the next chapter and jumps to __test_chapter_end
#         skip fast until label test_chapter_end timeout 180.0

#         python:
#             store.test.autorunner.reset()
