from conftest import *


class TestCreateOrder:

    @pytest.mark.parametrize(
        "color",
        [
            ([]),
            (["BLACK"]),
            (["GREY"]),
            (["BLACK", "GREY"])
        ]
    )

    @allure.title('Проверка создания заказа с различными вариантами увета самоката')
    def test_create_order(self, create_order_data, color):
        payload = create_order_data
        payload['color'] = color
        response_create = requests.post(Handles.handle_create_order, json=payload)

        assert response_create.status_code == 201 and 'track' in response_create.text
    @allure.title('Проверка получения списка заказов')
    def test_get_a_list_of_orders(self):
        response = requests.get(Handles.handle_create_order)
        assert response.status_code == 200 and 'orders' in response.text
