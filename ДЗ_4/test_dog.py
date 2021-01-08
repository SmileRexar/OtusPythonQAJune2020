import pytest
import requests
import json
import random

base_url = 'https://dog.ceo/api/breed'


def validate_json(text):
    return True if (json.loads(text)) else False


@pytest.mark.parametrize("code", [200])
def test_get_list_all(code):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    is_valid = validate_json(response.text)
    assert response.status_code == code
    assert is_valid, 'Получен json'


@pytest.mark.parametrize("url , code", [
    ('https://dog.ceo/api/breeds/image/random', 200),
    ('https://dog.ceo/api/breeds/image/random121', 404)
])
def test_get_random_image(url, code):
    response = requests.get(url)
    assert response.status_code == code


def test_sub_breeds():
    response = requests.get('https://dog.ceo/api/breed/hound/list')
    data_str = response.json().get('message')
    image_dog = random.choice(data_str)
    response = requests.get(f'https://dog.ceo/api/breed/hound/{image_dog}/images')
    assert response.status_code == 200


def test_get_hound_collention():
    response = requests.get('https://dog.ceo/api/breed/hound/images')
    data_str = response.json().get('message')
    assert len(data_str) > 1

#
#
# #Чек рандом картинку
# #Returns an array of all the images from a breed, e.g. hound
# response = requests.get('https://dog.ceo/api/breed/hound/images')
# print(response.text)
# print(response.status_code)
#
#
# #LIST ALL SUB-BREEDS
# response = requests.get('https://dog.ceo/api/breed/hound/list')
# print(response.text)
# print(response.status_code)
