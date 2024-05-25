import random
import string
from datetime import datetime
from datetime import datetime, timedelta
class DataGeneration:
    @staticmethod
    def generate_random_string(length=10):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def register_new_courier_and_return_login_password(self, length=10):
        #login_pass = []

        login = self.generate_random_string(length)
        password = self.generate_random_string(length)
        first_name = self.generate_random_string(length)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        return payload

    def generation_order_data(self, length=10):
        first_name = self.generate_random_string(length)
        last_name = self.generate_random_string(length)
        address = self.generate_random_string(length)
        comment = self.generate_random_string(length)

        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": random.randint(0, 6),
            "phone": f'8{random.randint(9000000000,9999999999)}',
            "rentTime": random.randint(0, 6),
            "deliveryDate": '2024-12-12',
            "comment": comment,
        }

        return payload



    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    #if response.status_code == 201:
    #   login_pass.append(login)
    #    login_pass.append(password)
    #    login_pass.append(first_name)

    # возвращаем список
    #return login_pass

