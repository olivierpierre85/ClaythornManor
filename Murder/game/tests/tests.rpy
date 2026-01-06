testsuite global:
    setup:
        pause until screen "main_menu" timeout 20.0

    before testsuite:
        pause until screen "main_menu" timeout 20.0
        run Start()

    teardown:
        exit
