import requests
import URLs
from conftest import data_generator
from conftest import user
import allure
import copy

class TestCreateUser:

    def test_create_user(self, data_generator):
        payload = copy.copy(data_generator)
        response = requests.post(URLs.URL_CREATE_USER, data=payload)
        assert response.status_code == 200

        access_token = response.json()['accessToken']

        requests.delete(URLs.URL_LOGIN_USER, headers={'Authorization': access_token})

    @allure.title('Проверка статус-кода при попытке создания двух одинаковых пользователей')
    @allure.description('Два раза создаются пользователи с одинаковыми данными и проверяется статус-код')
    def test_existing_user_status_code(self, user):
        payload = copy.copy(user)
        response = requests.post(URLs.URL_CREATE_USER, data=payload)
        assert response.status_code == 403

    @allure.title('Проверка текста ошибки при попытке создания двух одинаковых пользователей')
    @allure.description('Два раза создаются пользователи с одинаковыми данными и проверяется текст ошибки')
    def test_existing_user_message(self, user):
        payload = copy.copy(user)
        response = requests.post(URLs.URL_CREATE_USER, data=payload)
        assert response.json()['message'] == "User already exists"

    @allure.title('Проверка статус-кода при попытке создания пользователя с незаполненной почтой')
    @allure.description('Происходит попытка создать пользователя с пустым полем email, и проверяется статус-код')
    def test_create_user_no_email_status_code(self, user):
        payload = copy.copy(user)
        payload['email'] = ''
        response = requests.post(URLs.URL_CREATE_USER, data=payload)
        assert response.status_code == 403

    @allure.title('Проверка текста ошибки при попытке создания пользователя с незаполненной почтой')
    @allure.description('Происходит попытка создать пользователя с пустым полем email, и проверяется текст ошибки')
    def test_create_user_no_email_message(self, user):
        payload = copy.copy(user)
        payload['email'] = ''
        response = requests.post(URLs.URL_CREATE_USER, data=payload)
        assert response.json()['message'] == "Email, password and name are required fields"

    @allure.title('Проверка статус-кода при попытке создания пользователя с незаполненным именем')
    @allure.description('Происходит попытка создать пользователя с пустым полем name, и проверяется статус-код')
    def test_create_user_no_email_status_code(self, user):
        payload = copy.copy(user)
        payload['name'] = ''
        response = requests.post(URLs.URL_CREATE_USER, data=payload)
        assert response.status_code == 403

    @allure.title('Проверка текста ошибки при попытке создания пользователя с незаполненным именем')
    @allure.description('Происходит попытка создать пользователя с пустым полем name, и проверяется текст ошибки')
    def test_create_user_no_email_message(self, user):
        payload = copy.copy(user)
        payload['name'] = ''
        response = requests.post(URLs.URL_CREATE_USER, data=payload)
        assert response.json()['message'] == "Email, password and name are required fields"

    @allure.title('Проверка статус-кода при попытке создания пользователя с незаполненным паролем')
    @allure.description('Происходит попытка создать пользователя с пустым полем password, и проверяется статус-код')
    def test_create_user_no_email_status_code(self, user):
        payload = copy.copy(user)
        payload['password'] = ''
        response = requests.post(URLs.URL_CREATE_USER, data=payload)
        assert response.status_code == 403

    @allure.title('Проверка текста ошибки при попытке создания пользователя с незаполненным паролем')
    @allure.description('Происходит попытка создать пользователя с пустым полем password, и проверяется текст ошибки')
    def test_create_user_no_email_message(self, user):
        payload = copy.copy(user)
        payload['password'] = ''
        response = requests.post(URLs.URL_CREATE_USER, data=payload)
        assert response.json()['message'] == "Email, password and name are required fields"





