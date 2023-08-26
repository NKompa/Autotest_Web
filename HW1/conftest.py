import pytest
import requests
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    username, password, address = data['username'], data['password'], data['address']

S = requests.Session()


@pytest.fixture()
def user_login():
    res1 = S.post(url=address, data={'username': username, 'password': password})
    return res1.json()['token']


@pytest.fixture()
def post_title():
    return 'A title'


@pytest.fixture()
def post_title1():
    return 'Пост №1'


@pytest.fixture()
def post_description1():
    return 'Описание поста №1'


@pytest.fixture()
def post_content1():
    return 'Содержимое поста №1'
