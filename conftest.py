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

@pytest.fixture
def create_order(create_order_data):
    payload = create_order_data
    response_create = requests.post(Handles.handle_create_order, json=payload)
    track_order = response_create.json()['track']

    return track_order

@pytest.fixture
def login(create_courier):
    payload = create_courier
    response_login = requests.post(Handles.handle_login_courier, data=payload)
    id_courier = response_login.json()['id']

    return id_courier

@pytest.fixture
def get_order_id(create_order):
    track_order = create_order
    payload = {'t': track_order}

    response = requests.get(f'{Handles.handle_create_order}/track', params=payload)
    id_order = response.json()['order']['id']

    return id_order
