import unittest
import requests
from requests import exceptions
import io
from unittest.mock import patch
import sys

MAX_R_VALUE = 1000


# Тесты
class TestGetCurrencies(unittest.TestCase):

    def test_currency_usd(self):
        """
        Проверяет наличие ключа в словаре и значения этого ключа
        """
        currency_list = ['USD']
        currency_data = get_currencies(currency_list)

        self.assertIn(currency_list[0], currency_data)
        self.assertIsInstance(currency_data['USD'], float)
        self.assertGreaterEqual(currency_data['USD'], 0)
        self.assertLessEqual(currency_data['USD'], MAX_R_VALUE)

    def test_nonexist_code(self):
        self.assertIn("Код валюты", get_currencies(['XYZ'])['XYZ'])
        self.assertIn("XYZ", get_currencies(['XYZ'])['XYZ'])
        self.assertIn("не найден", get_currencies(['XYZ'])['XYZ'])

    def test_get_currency_error(self):
        error_phrase_regex = "Ошибка при запросе к API"
        currency_list = ['USD']

        with self.assertRaises(requests.exceptions.RequestException):
            currency_data = get_currencies(currency_list, url="https://")

        # Дополнение: захватываем вывод в stdout и проверяем наличие фразы с помощью assertRegex
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            with self.assertRaises(requests.exceptions.RequestException):
                get_currencies(currency_list, url="https://")
            output = mock_stdout.getvalue()
            self.assertRegex(output, error_phrase_regex)


# Запуск тестов
unittest.main(argv=[''], verbosity=2, exit=False)
