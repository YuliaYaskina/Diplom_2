import requests
import URLs
from conftest import user_login
import allure
import copy

from helpers.data_generator import DataGenerate


class TestOrderCreate:
    @allure.title('Проверка создания заказа авторизованным пользователем без ингредиентов')
    @allure.description('Происходит создания заказа авторизованным пользователем без ингредиентов и проверется статус-код')
    def test_order_create_with_auth_without_ingredients(self, user_login):
        access_token = copy.copy(user_login)
        payload = {"ingredients": []}
        response = requests.post(URLs.URL_CREATE_ORDER, headers={'Authorization': access_token}, data = payload)
        assert response.status_code == 400

    @allure.title('Проверка создания заказа с ингредиентами пользователем без авторизации')
    @allure.description('Происходит создание заказа с ингредиентами пользователем без авторизации и проверется статус-код')
    def test_order_create_no_auth_with_ingredients(self):
        response = requests.get(URLs.URL_GET_INGREDIENTS)
        r = response.json()
        ingredient = (r["data"][0]["_id"])
        payload = {"ingredients": [ingredient]}
        response = requests.post(URLs.URL_CREATE_ORDER, data=payload)
        assert response.status_code == 200

    @allure.title('Проверка создания заказа с ингредиентами авторизованным пользователем')
    @allure.description('Происходит создание заказа с ингредиентами авторизованным пользователем и проверется статус-код')
    def test_order_create_with_auth_with_ingredients(self, user_login):
        access_token = copy.copy(user_login)
        response = requests.get(URLs.URL_GET_INGREDIENTS)
        ingredient = (response.json()["data"][0]["_id"])
        payload = {"ingredients": [ingredient]}
        response = requests.post(URLs.URL_CREATE_ORDER, data=payload, headers={'Authorization': access_token})
        assert response.status_code == 200

    @allure.title('Проверка создания заказа авторизованным пользователем с некорректным id ингредиента')
    @allure.description('Происходит создание заказа авторизованным пользователем с некорректным id ингредиента и проверется статус-код')
    def test_order_create_with_auth_wrong_id(self, user_login):
        access_token = copy.copy(user_login)
        ingredient = DataGenerate.generate_random_string(10)
        payload = {"ingredients": [ingredient]}
        response = requests.post(URLs.URL_CREATE_ORDER, data=payload, headers={'Authorization': access_token})
        assert response.status_code == 500
