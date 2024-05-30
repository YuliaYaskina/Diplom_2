import requests
import URLs
from conftest import data_generator
from conftest import user_login
import allure
import copy


class TestUserEdit:
    @allure.title('Проверка стутус-кода при изменении данных авторизованного пользователя')
    @allure.description('Проверяется статус-код при попытке изменить электронную почту, имя и пароль авторизованного пользователя')
    def test_edit_name_email_password_with_auth(self, user_login, data_generator):
        access_token = copy.copy(user_login)
        payload = copy.copy(data_generator)
        response = requests.patch(URLs.URL_EDIT_USER, data=payload, headers={'Authorization': access_token})
        assert response.status_code == 200

    @allure.title('Проверка корректности возвращаемых полей email и name при изменении данных авторизованного пользователя')
    @allure.description('Проверяется корректность возвращаемых полей email и name при попытке изменить электронную почту, имя и пароль авторизованного пользователя')
    def test_edit_name_email_password_with_auth(self, user_login, data_generator):
        access_token = copy.copy(user_login)
        payload = copy.copy(data_generator)
        response = requests.patch(URLs.URL_EDIT_USER, data=payload, headers={'Authorization': access_token})
        assert response.json()['email'] == payload['email'] and response.json()['name'] == payload['name']

    @allure.title('Проверка успешности изменения данных авторизованного пользователя')
    @allure.description('Проверяется значение поля success при попытке изменить электронную почту, имя и пароль авторизованного пользователя')
    def test_edit_name_email_password_with_auth(self, user_login, data_generator):
        access_token = copy.copy(user_login)
        payload = copy.copy(data_generator)
        response = requests.patch(URLs.URL_EDIT_USER, data=payload, headers={'Authorization': access_token})
        assert response.json()['success'] == True

    @allure.title('Проверка статус-кода при изменении данных неавторизованного пользователя')
    @allure.description('Проверяется статус-код при попытке изменить электронную почту, имя и пароль неавторизованного пользователя')
    def test_edit_name_email_password_without_auth(self, data_generator):
        payload = copy.copy(data_generator)
        response = requests.patch(URLs.URL_EDIT_USER, data=payload)
        assert response.status_code == 401

    @allure.title('Проверка текста ошибки при изменении данных неавторизованного пользователя')
    @allure.description('Проверяется текст ошибки при попытке изменить электронную почту, имя и пароль неавторизованного пользователя')
    def test_edit_name_email_password_without_auth(self, data_generator):
        payload = copy.copy(data_generator)
        response = requests.patch(URLs.URL_EDIT_USER, data=payload)
        assert response.json()['message'] == 'You should be authorised'


    @allure.title('Проверка неуспешности ошибки при изменении данных неавторизованного пользователя')
    @allure.description('Проверяется значение поля success при попытке изменить электронную почту, имя и пароль неавторизованного пользователя')
    def test_edit_name_email_password_without_auth(self, data_generator):
        payload = copy.copy(data_generator)
        response = requests.patch(URLs.URL_EDIT_USER, data=payload)
        assert response.json()['success'] == False




