import requests
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    address = data['address_posts']

S = requests.Session()


def test_rest(user_login, post_title):
    result = S.get(url=address, headers={"X-Auth-Token": user_login}, params={'owner': 'notMe'}).json()['data']
    r = [i['title'] for i in result]
    assert post_title in r, 'Test_rest FAILED'


def test_post(user_login, post_title1, post_description1, post_content1):
    post_data = {
        'title': post_title1,
        'description': post_description1,
        'content': post_content1
    }
    response = S.post(url=address, headers={"X-Auth-Token": user_login}, json=post_data)
    assert response.status_code == 200, 'Не удалось создать новый пост'

    result = S.get(url=address, headers={"X-Auth-Token": user_login}).json()['data']
    descriptions = [i['description'] for i in result]
    assert post_description1 in descriptions, 'Новый пост не найден на сервере'
