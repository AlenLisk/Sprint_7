from conftest import *


class TestDeleteCourier:
    @allure.title('Проверка удаления курьера')
    def test_delete_courier(self, login):
        id_courier = login
        response = requests.delete(f'{Handles.handle_create_courier}/{id_courier}')

        assert response.status_code == 200 and response.text == '{"ok":true}'
    @allure.title('Проверка удаления курьера без id')
    def test_delete_courier_without_id(self, login):
        id_courier = ''
        response = requests.delete(f'{Handles.handle_create_courier}/{id_courier}')

        assert response.status_code == 404
    @allure.title('Проверка удаления курьера с невалидным id')
    def test_delete_courier_with_incorrect_id(self):
        response = requests.delete(f'{Handles.handle_create_courier}/56421344')

        assert response.status_code == 404 and 'Курьера с таким id нет' in response.text
