import json

import pytest
import requests

from OtusPythonQA.HW04.lib.helpers import assert_valid_schema


@pytest.mark.parametrize("post_id , code_response, res_not_empty", [
    ('0', 404, False),
    ('1', 200, True),
    ('100', 200, True),
    ('-4', 404, False),
])
def test_get_post(start_url, post_id, code_response, res_not_empty):
    url = f'{start_url}/posts/{post_id}'
    resp = requests.get(url)
    assert resp.status_code == code_response

    if res_not_empty:
        assert_valid_schema(resp.json(), './schemas/posts.json')
    else:
        assert_valid_schema(resp.json(), 'schemas/empty.json')


def test_listing_all_resources(start_url):
    url = f'{start_url}/posts'
    resp = requests.get(url)
    assert resp.status_code == 200
    assert_valid_schema(resp.json(), 'schemas/listing_resources.json')


@pytest.mark.parametrize("data , code_response", [
    (
            {
                'title': 'foo1',
                'body': 'bar1',
                'userId': 123
            },
            201),
    (
            {
                'title': 'fd3af2f21g2e3gd',
                'body': '1dd3d3ddf5fdd3ddd5dd3ddd4dd4ddd5dd5d4dd5d3dd4ddd5ddd3d',
                'userId': 12433524545
            },
            201),
])
def test_create_resource(start_url, data, code_response):
    url = f'{start_url}/posts'
    headers = {
        'Content-type': 'application/json',
        'charset': 'UTF-9'}
    resp = requests.post(
        url,
        data=json.dumps(data),
        headers=headers
    )
    assert resp.status_code == code_response
    j = resp.json()
    # assert j['title'] == data['title']
    # assert j['body'] == data['body']
    # assert j['userId'] == data['userId']
    for i in data.keys():
        assert j[i] == data[i]

    max_resource_in_list = 100
    assert j['id'] == max_resource_in_list + 1


@pytest.mark.parametrize("data , code_response", [
    (
            {
                'post_id': '2',
                'title': 'foo',
                'body': 'bar',
                'userId': '123'
            },
            200),
    (
            {
                'post_id': '15615',
                'title': 'foo',
                'body': f'bar',
                'userId': '123'
            },
            500),
])
def test_update(session, start_url, data, code_response):
    post_id = data['post_id']
    res = session.put(url=f'{start_url}/posts/{post_id}', data=data)
    assert res.status_code == code_response
    # позитивные сценарии
    if res.status_code in [200]:
        res_json = res.json()
        print(res_json)
        # assert res_json['title'] == data['title']
        # assert res_json['body'] == data['body']
        for i in data.keys():
            assert res_json[i] == data[i]


@pytest.mark.parametrize("data , code_response", [
    (
            {
                'post_id': '-1',
                'title': 'foo',
                'body': 'bar',
                'userId': '123'
            },
            500)

])
def test_update_negative(session, start_url, data, code_response):
    post_id = data['post_id']
    res = session.put(url=f'{start_url}/posts/{post_id}', data=data)
    assert res.status_code == code_response


@pytest.mark.parametrize("data , code_response", [
    (
            {
                'post_id': '2',
                'title': 'foo',
            },
            200),
    (
            {
                'post_id': '100',
                'title': 'faffing',
            },
            200),

])
def test_update_with_patch(session, start_url, data, code_response):
    post_id = data['post_id']
    res = session.patch(url=f'{start_url}/posts/{post_id}', data=data)
    assert res.status_code == code_response
    res_json = res.json()
    for i in data.keys():
        assert res_json[i] == data[i]
    assert_valid_schema(res_json, './schemas/posts.json')


@pytest.mark.parametrize("post_id , code_response", [
    (1, 200),
    (-1, 200),
    (1000, 200),
])
def test_delete_post(session, start_url, post_id, code_response):
    # rand_id = random.randint(1, 100)
    url = f'{start_url}/posts/{post_id}'
    resp = requests.delete(url)
    assert resp.status_code == code_response


@pytest.mark.parametrize("user_id , code_response", [
    (1, 200),
    (10, 200),
    (3, 200),

])
def test_check_filter_resources(session, start_url, user_id, code_response):
    res = session.get(url=f'{start_url}/posts/?userId={user_id}')
    a_json = res.json()
    for i in a_json:
        assert i['userId'] == user_id


def test_check_schema(session, start_url):
    url = f'{start_url}/todos'
    resp = requests.get(url)
    assert resp.status_code == 200
    assert_valid_schema(resp.json(), './schemas/todos.json')
