import pytest
import requests

start_url = 'https://api.openbrewerydb.org/breweries'


@pytest.mark.parametrize("key_word , code_response", [
    ('dog', 200),
    ('dog111', 200),
    ('fox---', 200),
])
def test_search(key_word, code_response):
    url = f'{start_url}/search?query={key_word}'
    response = requests.get(url)
    assert response.status_code == code_response


def test_breeds_responce_time():
    url = f'{start_url}/breeds/list/all'
    resp = requests.get(url)
    assert resp.elapsed.seconds < 0.7

@pytest.mark.parametrize("key_word , code_response", [
    ('dog', 200),
    ('dog111', 200),
    ('fox---', 200),
])
def test_search_with_groupby(key_word, code_response):
    url = f'{start_url}/search?query={key_word}'
    response = requests.get(url)
    assert response.status_code == code_response


def test_autocomplete():
    url = f'{start_url}/autocomplete?query=dog'
    max_list_size = 15
    response = requests.get(url).json()
    assert len(response) <= max_list_size, 'Проверка получения максимум 15 элементов'


@pytest.mark.parametrize("id_key , status_code", [
    ('5494', 200),
    ('5494000001', 404),
])
def test_single_brewery(id_key, status_code):
    url = f'{start_url}/{id_key}'
    response = requests.get(url)
    assert response.status_code == status_code, f'Сервис вернул 200'
