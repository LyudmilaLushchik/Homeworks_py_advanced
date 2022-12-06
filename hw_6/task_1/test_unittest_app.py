import unittest
from parameterized import parameterized
from app import *
from fixtures import *
from unittest import mock


class TestFunctions(unittest.TestCase):

    def setUp(self) -> None:
        print("setUp ---> START TEST")

    def tearDown(self) -> None:
        print("setUp ---> STOP TEST")

    @parameterized.expand(fixture_check_doc_existance)
    def test_check_document_existance(self, doc_number, fixt_result):
        self.assertEqual(check_document_existance(doc_number), fixt_result)

    def test_get_all_doc_owners_names(self):
        self.assertEqual(get_all_doc_owners_names(), fixture_get_all_doc_owners_names)

    @parameterized.expand(fixture_get_doc_owner_name)
    def test_get_doc_owner_name(self, number, fixt_result):
        with mock.patch('builtins.input', return_value = number):
            self.assertEqual(get_doc_owner_name(), fixt_result)

    @parameterized.expand(fixture_show_doc_info)
    def test_show_doc_info(self, document, fixt_result):
        self.assertEqual(show_document_info(document), fixt_result)

    @parameterized.expand(fixture_get_doc_shelf)
    def test_get_doc_shelf(self, number, fixt_result):
        with mock.patch('builtins.input', return_value = number):
            result = get_doc_shelf()
            self.assertEqual(result, fixt_result)
    
    @parameterized.expand(fixture_add_new_doc)
    def test_add_new_doc(self, new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number, fixt_result):
        with mock.patch('builtins.input', side_effect = [new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number]):
            self.assertEqual(add_new_doc(), fixt_result)

    @parameterized.expand(fixture_delete_doc)
    def test_delete_doc(self, doc_number, fixt_result):
        with mock.patch('builtins.input', return_value = doc_number):
            self.assertEqual(delete_doc(), fixt_result)

    @parameterized.expand(fixture_remove_doc_from_shelf)
    def test_remove_doc_from_shelf(self, doc_number, fixt_result):
        self.assertEqual(remove_doc_from_shelf(doc_number), fixt_result)

    @parameterized.expand(fixture_add_new_shelf)
    def test_add_new_shelf(self, shelf_number, fixt_result):
        with mock.patch('builtins.input', return_value = shelf_number):
           self.assertEqual(add_new_shelf(), fixt_result)