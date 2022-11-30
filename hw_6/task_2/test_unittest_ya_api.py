import unittest
from configparser import ConfigParser
from parameterized import parameterized
from ya_api import create_folder


conf = ConfigParser()
conf.read('settings.ini')
token = conf['Yandex']['token']

fixture = [
    ('folder_test_1', token, 201),
    ('folder_test_2', 'incorrect_token', 401)
]


class TestYaDisk(unittest.TestCase):           

    @parameterized.expand(fixture)
    def test_create_folder(self, path, token, fixt_result):
        self.assertEqual(create_folder(token, path), fixt_result)