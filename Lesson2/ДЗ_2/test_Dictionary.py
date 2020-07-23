import pytest


@pytest.fixture
def get_dict_mock():
    """
    Функция замещающая теструемую структуру
    :return: пустой словарь
    """
    return {}


@pytest.mark.parametrize("input_item , expected_len", [
    ({'iphone 3G': 2008, 'iphone 4S': 2011,
      'iphone 3GS': 2009, 'iphone 5': 2012,
      'iphone 4': 2010, 'android 10': 2019
      }, 6),
    ({"Alex": 1, 'Alex ': 2
      }, 2)
])
def test_add_items(input_item, expected_len, get_dict_mock):
    get_dict_mock.update(input_item)
    assert len(get_dict_mock) == expected_len


def test_delete_item(get_dict_mock):
    get_dict_mock['Test1'] = "1"
    get_dict_mock['Test2'] = "2"
    get_dict_mock['Test3'] = "3"
    del get_dict_mock['Test2']
    assert len(get_dict_mock) ==2
