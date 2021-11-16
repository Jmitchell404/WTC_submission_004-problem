import unittest
from test_base import run_unittests
from unittest.mock import patch
from super_algos import *
class TestSuperAlgos(unittest.TestCase):
    def test_find_min(self):
        """
        Tests Find_min if the minimum element is being found and bring deleted.
        """
        test_list = [21,420,69,999,18,911]
        self.assertEqual(find_min(test_list), min(test_list))


    def test_empty_list(self):
        """
        Tests find_min if the list is empty and will return -1.
        """
        test_list = []
        self.assertEqual(find_min(test_list), -1)


    def test_non_ints(self):
        """
        Tests find_min for if there are non_ints in the list and will return -1.
        """
        test_list = ["string", True, False]
        self.assertEqual(find_min(test_list), -1)


    def test_sum_all(self):
        """
        Tests sum_all if there are ints in the list.
        """
        test_list = [21,420,69,999,18,911]
        self.assertEqual(sum_all(test_list), sum(test_list))


    def test_character_set(self):
        """
        Tests sum_all if the list is empty and will return -1.
        """
        test_list = []
        self.assertEqual(sum_all(test_list), -1)


    def test_invalid_elements(self):
        """
        Tests sum_all for non ints and returns -1.
        """
        test_list = ["invalid", "True", "False"]
        self.assertEqual(sum_all(test_list), -1)

    def test_character_set(self):
        """
        Tests find_possible_strings for if the list is empty and will return -1.
        """
        test_list = []
        self.assertEquals(find_possible_strings(test_list, 1), [])


    def find_possible_strings(self):
        """
        Tests find_possible_strings for if there are letters in the list.
        """
        test_list = ['a','b','c','d']
        self.assertEqual(find_possible_strings(test_list, 1), 1)