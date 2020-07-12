import pytest


@pytest.fixture
def get_set_mock():
    """
    Функция замещающая теструемую структуру
    :return: пустой set()
    """
    return set()


@pytest.mark.parametrize("input_item , expected_len", [
    ((1, 2, 3, 4), 4),
    ((1, ';', '3', 4), 4),
    ((1, '1', '1', 1), 2),
    ((1, 'A', 'a', 1), 3)

])
def test_add_items(input_item, expected_len, get_set_mock):
    for _ in input_item:
        get_set_mock.add(_)
    assert len(get_set_mock) == expected_len
