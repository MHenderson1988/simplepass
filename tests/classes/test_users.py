from unittest import TestCase
from main.classes.users import Users


class TestUsers(TestCase):
    def test_change_name(self):
        user = Users("Dave")
        list_of_names = ["Mark", "Terry", "Mike"]
        for i in list_of_names:
            user.change_name(i)
            self.assertEqual(user.name, i)

    def test_add_password(self):
        user = Users("Mark")
        website_list = ["hello.com", "goodbye.com", "google.com", "testing.com"]
        pass_list = ["123", "321", "hello", "password"]
        expected_result = {'hello.com': '123', 'goodbye.com': '321', 'google.com': 'hello', 'testing.com': 'password'}
        i = 0
        while i < len(website_list):
            user.add_password(website_list[i], pass_list[i])
            i += 1
        self.assertEqual(user.password_list, expected_result)