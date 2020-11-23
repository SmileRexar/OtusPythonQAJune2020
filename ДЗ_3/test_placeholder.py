import random
import requests
import re


start_url = 'https://jsonplaceholder.typicode.com/'


def test_delete_random_post():
    rand_id = random.randint(1, 100)
    url = f'{start_url}posts/{rand_id}'
    resp = requests.get(url)
    assert resp.status_code == 200


def valid_email(email):
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))


def test_get_comment():
    url = f'{start_url}comments'
    resp = requests.get(url)
    text = resp.json()
    rand_id = random.randint(1, 100)
    assert valid_email(text[rand_id]['email']), 'Не прошла валидация'
    assert resp.status_code == 200


def test_get_random_post():
    rand_id = random.randint(1, 100)
    url = f'{start_url}posts/{rand_id}'
    print(url)
    resp = requests.get(url)
    assert resp.status_code == 200
