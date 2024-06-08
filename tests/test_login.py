import requests
import URLs
from conftest import registration_data_generator
from conftest import create_user
import allure
import copy

class TestLogin:
    @allure.title('Проверка логина существующего пользователя')
    @allure.description('Создается новый пользователь и проверяется его логин')
    def test_login(self, create_user):
        payload = copy.copy(create_user)
        response = requests.post(URLs.URL_LOGIN_USER, data=payload)
        assert response.status_code == 200

    @allure.title('Проверка статус-кода при логине с невалидным логином и паролем')
    @allure.description('Проверяется статус-код при логине с некорректным логином и паролем')
    def test_login_incorrect_login_and_password_status_code(self, registration_data_generator):
        payload = copy.copy(registration_data_generator)
        payload_for_login = {"email": payload['email'], "password": payload['password']}
        response = requests.post(URLs.URL_LOGIN_USER, data=payload_for_login)
        assert response.status_code == 401

    @allure.title('Проверка сообщения об ошибке при логине с невалидным логином и паролем')
    @allure.description('Проверяется сообщение об ошибке при логине с некорректным логином и паролем')
    def test_login_incorrect_login_and_password_status_code(self, registration_data_generator):
        payload = copy.copy(registration_data_generator)
        payload_for_login = {"email": payload['email'], "password": payload['password']}
        response = requests.post(URLs.URL_LOGIN_USER, data=payload_for_login)
        assert response.json()['message'] == "email or password are incorrect"

