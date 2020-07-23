import pytest


@pytest.fixture
def get_str_mock():
    """
    Функция замещающая теструемую структуру
    :return: пустой str()
    """
    return ""


@pytest.mark.parametrize("input_item , expected_len, expected_res", [
    ("1,2,3", 5, '1,2,3'),
    (("HELLO"), 5, "HELLO")

])
def test_add_items(input_item, expected_len, expected_res, get_str_mock):
    assert get_str_mock + input_item == expected_res
    assert len(input_item) == expected_len


@pytest.mark.parametrize("input_str , template_char, expected_res", [
    ("HELLO", 'LL', "HEO"),
    ("heLlOa", 'L', "helOa")

])
def test_delete_character(get_str_mock, input_str, template_char, expected_res):
    assert input_str.replace(template_char, "") == expected_res
