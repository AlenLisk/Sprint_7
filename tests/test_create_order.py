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
    def test_create_order(self, create_order_data, color):
        payload = create_order_data
        payload['color'] = color
        response_create = requests.post(Handles.handle_create_order, json=payload)

        assert response_create.status_code == 201 and 'track' in response_create.text





