from conftest import *


class TestAcceptOrder:
    @allure.title('Проверка принятия заказа')
    def test_accept_order(self, login, get_order_id):
        id_courier = login
        id_order = get_order_id

        payload = {'courierId': id_courier}
        response = requests.put(f'{Handles.handle_create_order}/accept/{id_order}', params=payload)

        assert response.status_code == 200 and '{"ok":true}' in response.text
    @allure.title('Проверка принятия заказа без id курьера')
    def test_accept_order_without_id_courier(self, get_order_id):
        id_order = get_order_id

        payload = {'courierId': ""}
        response = requests.put(f'{Handles.handle_create_order}/accept/{id_order}', params=payload)

        assert response.status_code == 400 and 'Недостаточно данных' in response.text
    @allure.title('Проверка принятия заказа с невалидным id курьера')
    def test_accept_order_with_incorrect_id_courier(self, get_order_id):
        id_order = get_order_id

        payload = {'courierId': "000485"}
        response = requests.put(f'{Handles.handle_create_order}/accept/{id_order}', params=payload)

        assert response.status_code == 404 and 'Курьера с таким id не существует' in response.text
    @allure.title('Проверка принятия заказа без id заказа')
    def test_accept_order_without_id_order(self, login):
        id_order = ''
        id_courier = login

        payload = {'courierId': id_courier}
        response = requests.put(f'{Handles.handle_create_order}/accept/{id_order}', params=payload)

        assert response.status_code == 404 and 'Not Found' in response.text
    @allure.title('Проверка принятия заказа с неккоректным id заказа')
    def test_accept_order_with_incorrect_id_order(self, login):
        id_order = '00589200'
        id_courier = login

        payload = {'courierId': id_courier}
        response = requests.put(f'{Handles.handle_create_order}/accept/{id_order}', params=payload)

        assert response.status_code == 404 and 'Заказа с таким id не существует' in response.text
