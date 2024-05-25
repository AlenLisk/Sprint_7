import pytest
from data_gen import DataGeneration
import requests
from handles import Handles

@pytest.fixture
def create_payload():
    data_generation = DataGeneration()
    payload = data_generation.register_new_courier_and_return_login_password()

    return payload

@pytest.fixture
def create_courier(create_payload):
    payload = create_payload
    response_create = requests.post(Handles.handle_create_courier, data=payload)
    del payload['firstName']

    return payload

@pytest.fixture
def create_order_data():
    data_generation = DataGeneration()
    payload = data_generation.generation_order_data()

    return payload
