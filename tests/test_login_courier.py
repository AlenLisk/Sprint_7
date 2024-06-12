from conftest import *
import requests


class TestLoginCourier:
    @allure.title('Проверка логина курьера')
    def test_courier_login(self, create_courier):
        payload = create_courier
        response_login = requests.post(Handles.handle_login_courier, data=payload)

        assert response_login.status_code == 200 and 'id' in response_login.text
    @allure.title('Проверка логина без логина')
    def test_courier_login_without_login(self, create_courier):
        payload = create_courier
        payload['login'] = ''
        response_login = requests.post(Handles.handle_login_courier, data=payload)

        assert response_login.status_code == 400 and 'Недостаточно данных' in response_login.text
    @allure.title('Проверка логина без пароля')
    def test_courier_login_without_password(self, create_courier):
        payload = create_courier
        payload['password'] = ''
        response_login = requests.post(Handles.handle_login_courier, data=payload)

        assert response_login.status_code == 400 and 'Недостаточно данных' in response_login.text
    @allure.title('Проверка логина с невалидным логином')
    def test_courier_login_with_invalid_login(self, create_payload):
        payload = create_payload
        payload['login'] = 'invalid_login'
        response_login = requests.post(Handles.handle_login_courier, data=payload)

        assert response_login .status_code == 404 and 'Учетная запись не найдена' in response_login.text
    @allure.title('Проверка логина с невалидным паролем')
    def test_courier_login_with_invalid_password(self, create_payload):
        payload = create_payload
        payload['password'] = 'invalid_password'
        response_login = requests.post(Handles.handle_login_courier, data=payload)

        assert response_login .status_code == 404 and 'Учетная запись не найдена' in response_login.text
    @allure.title('Проверка логина с несуществующим курьером')
    def test_unregistered_courier_login(self):
        payload = {}
        payload['login'] = 'non-existent_login'
        payload['password'] = '1234'
        response_login = requests.post(Handles.handle_login_courier, data=payload)

        assert response_login .status_code == 404 and 'Учетная запись не найдена' in response_login.text
        