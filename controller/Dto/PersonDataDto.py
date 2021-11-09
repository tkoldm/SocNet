class PersonDataDto:

    def __init__(self, name: str, last_name: str, birtday: str,
                    phone_number: str, email: str, gender: int, password: str, position: str, second_name=None):
        self.data = {
            'name': name,
            'second_name': second_name,
            'last_name': last_name,
            'birtday': birtday,
            'phone_number': phone_number,
            'email': email,
            'gender': gender,
            'password': password,
            'position': position,
        }