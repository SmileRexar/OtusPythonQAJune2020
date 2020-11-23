import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://yandex.ru/",
        help="This is request url"
    )

    parser.addoption(
        "--status_code",
        default=200,
        type=int,
        help="This isresponce code"
    )

@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")
