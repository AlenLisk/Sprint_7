from conftest import *


class TestCreateCourier:
    def test_create_courier(self, create_payload):
        payload = create_payload
        response_create = requests.post(Handles.handle_create_courier, data=payload)

        assert response_create.status_code == 201 and response_create.text == '{"ok":true}'

    def test_create_two_identical_couriers(self, create_payload):
        payload = create_payload
        response_create = requests.post(Handles.handle_create_courier, data=payload)
        response_conflict = requests.post(Handles.handle_create_courier, data=payload)

        assert response_conflict.status_code == 409 and 'логин уже используется' in response_conflict.text

    def test_create_courier_without_login(self, create_payload):
        payload = create_payload
        payload['login'] = ''
        response_create = requests.post(Handles.handle_create_courier, data=payload)

        assert response_create.status_code == 400 and 'Недостаточно данных' in response_create.text

    def test_create_courier_without_password(self, create_payload):
        payload = create_payload
        payload['password'] = ''
        response_create = requests.post(Handles.handle_create_courier, data=payload)

        assert response_create.status_code == 400 and 'Недостаточно данных' in response_create.text
