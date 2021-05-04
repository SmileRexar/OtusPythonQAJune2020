import pytest
from selenium import webdriver

from ClientSSH import ClientSSH

HOST = "172.30.251.182"


@pytest.fixture(scope="function")
def ssh_session():
    # old HOST = "172.30.250.222"
    port = "22"
    username = "test"
    password = "test1"
    client_ssh = ClientSSH(
        HOST,
        port,
        username,
        password
    )
    return client_ssh


@pytest.fixture
def browser():
    wd = webdriver.Chrome()
    yield wd
    wd.quit()


@pytest.fixture(scope="module")
def start_url():
    return f'http://{HOST}'
