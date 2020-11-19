from unittest import TestCase
from main.gui_functions import update_user_list


class TestGuiFunctions(TestCase):
    def test_update_user_list(self):
        list_to_pass = []
        expected_result = ["Adam", "Mark"]
        list_to_pass = update_user_list(list_to_pass, "Mark")
        list_to_pass = update_user_list(list_to_pass, "Adam")
        names = [user.name for user in list_to_pass]
        self.assertEqual(expected_result, names)