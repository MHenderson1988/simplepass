from unittest import TestCase
from main.classes.users import Users

website_list = ["hello.com", "goodbye.com", "google.com", "testing.com"]
pass_list = ["123", "321", "hello", "password"]


class TestUsers(TestCase):
    def test_change_name(self):
        user = Users("Dave")
        list_of_names = ["Mark", "Terry", "Mike"]
        for i in list_of_names:
            user.change_name(i)
            self.assertEqual(user.name, i)

    def test_add_password(self):
        user = Users("Mark")
        expected_result = {'hello.com': '123', 'goodbye.com': '321', 'google.com': 'hello', 'testing.com': 'password'}
        i = 0
        while i < len(website_list):
            user.add_password(website_list[i], pass_list[i])
            i += 1
        self.assertEqual(user.password_list, expected_result)

    def test_remove_website(self):
        user = Users("Mark")
        expected_result = {'google.com': 'hello', 'testing.com': 'password'}
        i = 0
        while i < len(website_list):
            user.add_password(website_list[i], pass_list[i])
            i += 1
        user.remove_website("hello.com")
        user.remove_website("goodbye.com")
        self.assertEqual(user.password_list, expected_result)

    def test_edit_website_name(self):
        user = Users("Mark")
        expected_result = {'goodbye.co.uk': '321', 'google.com': 'hello', 'testing.com': 'password', 'hello.co.uk':
            '123'}
        i = 0
        while i < len(website_list):
            user.add_password(website_list[i], pass_list[i])
            i += 1
        user.edit_website_name('hello.com', 'hello.co.uk')
        print(user.password_list)
