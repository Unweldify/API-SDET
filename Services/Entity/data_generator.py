from random import randint


class Generator:
    """Класс генератор для создания данных"""
    def generate_client_data():
        """
        Генерирует данные клиента
        :return: Возвращает словарь данных клиента
        """
        title = ''
        for _ in range(1, randint(4,10)):
            title += chr(randint(97,122))
        return {
            'addition': {
                'additional_info': 'Дополнительные сведения',
                'additional_number': randint(0,10)
            },
            'important_numbers': [randint(0,99) for _ in range(randint(1,3))],
            'title': title,
            'verified': True
            }
