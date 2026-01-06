testsuite global:
    setup:
        pause until screen "main_menu" timeout 20.0

    before testcase:
        pause until screen "main_menu" timeout 20.0
        run Start()

    after testcase:
        $ renpy.full_restart()

    teardown:
        exit
