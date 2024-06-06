import pytest
import requests
import URLs
from helpers.data_generator import DataGenerate
import copy


@pytest.fixture
def registration_data_generator():
    email = f'{DataGenerate.generate_random_string(10)}@yandex.ru'
    password = DataGenerate.generate_random_string(10)
    name = DataGenerate.generate_random_string(10)
    payload = {"email": email, "password": password, "name": name}
    return payload

@pytest.fixture
def create_user(registration_data_generator):
    payload = copy.copy(registration_data_generator)
    response = requests.post(URLs.URL_CREATE_USER, data=payload)
    access_token = response.json()['accessToken']
    yield payload

    requests.delete(URLs.URL_LOGIN_USER, headers={'Authorization': access_token})

@pytest.fixture
def user_login(registration_data_generator, create_user):
    payload_for_login = {"email": create_user['email'], "password": create_user['password']}
    response = requests.post(URLs.URL_LOGIN_USER, data=payload_for_login)
    access_token = response.json()['accessToken']
    yield access_token

    requests.delete(URLs.URL_LOGIN_USER, headers={'Authorization': access_token})



