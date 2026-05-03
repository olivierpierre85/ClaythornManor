# --------------------------------------------
#   Host
#
#   Friday - Evening
#
#   Stub chapter — no content yet. Exists so the test runner detects the
#   chapter change and ends the friday_afternoon test cleanly.
# --------------------------------------------
label host_day1_evening:

    call change_time(18, 0, 'Evening', 'Friday', hide_minutes=True, chapter='friday_evening')

    jump work_in_progress
