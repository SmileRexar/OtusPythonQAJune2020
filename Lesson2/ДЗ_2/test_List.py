from random import random

import pytest


@pytest.fixture
def get_list_mock():
    """
    Функция замещающая теструемую структуру
    :return: пустой list
    """
    return []


@pytest.mark.parametrize("input_item , expected_len", [
    ([1, 2, 3, 4], 4),
    ([1, ';', '3', 4], 4),
    ([i for i in range(1, 11)], 10)
])
def test_add_items(input_item, expected_len, get_list_mock):
    for _ in input_item:
        get_list_mock.append(_)
    assert len(get_list_mock) == expected_len
    assert expected_len in get_list_mock


def test_remove_items(get_list_mock):
    get_list_mock.append(1)
    get_list_mock.append(2)
    get_list_mock.append(3)
    get_list_mock.remove(2)
    assert 2 not in get_list_mock
    assert len(get_list_mock) == 2
