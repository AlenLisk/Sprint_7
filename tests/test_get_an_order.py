from conftest import *


class TestGetOrder:
    def test_get_an_order(self, create_order):
        track_order = create_order
        payload = {'t': track_order}

        response = requests.get(f'{Handles.handle_create_order}/track', params=payload)

        assert response.status_code == 200 and response.json()['order']['track'] == track_order

    def test_gat_an_order_without_track(self, create_order):
        response = requests.get(f'{Handles.handle_create_order}/track')

        assert response.status_code == 400 and 'Недостаточно данных' in response.text

    def test_gat_an_order_with_incorrect_track(self, create_order):
        payload = {'t': '000415745'}
        response = requests.get(f'{Handles.handle_create_order}/track', params=payload)

        assert response.status_code == 404 and 'Заказ не найден' in response.text


