from conftest import *


class TestDeleteCourier:
    def test_delete_courier(self, login):
        id_courier = login
        response = requests.delete(f'{Handles.handle_create_courier}/{id_courier}')

        assert response.status_code == 200 and response.text == '{"ok":true}'

    def test_delete_courier_without_id(self, login):
        response = requests.delete(f'{Handles.handle_create_courier}/')

        assert response.status_code == 404

    def test_delete_courier_with_incorrect_id(self):
        response = requests.delete(f'{Handles.handle_create_courier}/56421344')

        assert response.status_code == 404 and 'Курьера с таким id нет' in response.text
