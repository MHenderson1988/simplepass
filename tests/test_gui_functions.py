from unittest import TestCase
from main.gui_functions import update_user_list

class TestGuiFunctions(TestCase):
    def test_update_user_list(self):
        list_to_pass = ["Mark", "Troy", "Fred"]