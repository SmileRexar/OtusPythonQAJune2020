import pytest
import requests


@pytest.fixture(scope="module")
def session():
    return requests.Session()

@pytest.fixture(scope="module")
def start_url(request):
    return request.config.getoption("--url")


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://jsonplaceholder.typicode.com",
        help="Request base url"
    )