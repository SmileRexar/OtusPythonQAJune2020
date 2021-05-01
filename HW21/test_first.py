def test_check_restart(ssh_session, browser, start_url):
    ssh_session.connect()

    stin, stout, ster = ssh_session.exec_command(" echo 'Yeeep. We have connection'")
    print(stout.read().decode("utf-8"))

    # opencart на apache поднят
    cmd_restart = 'sudo service apache2 restart'
    stin, stout, ster = ssh_session.exec_command(cmd_restart)
    for line in stout.read().decode("utf-8").splitlines():
        print(line)

    browser.get(start_url)
    # Проверяем титл страницы

    page_title = browser.title
    assert page_title == "Your Store"
