from unittest import TestCase

from main.password_generator import generate_password, populate_string, check_one_of_each_character


class TestPasswordGenerator(TestCase):
    def test_generate_password(self):
        exception_tuple = (TypeError, AssertionError)
        test_input = [2, "Hello", 28382, "This is a test"]
        for i in test_input:
            self.assertRaises(exception_tuple, generate_password, i)

    def test_populate_string(self):
        test_input_correct = [['j', '!', '3', 'N'], ['m', 'M', '~', '3']]
        test_input_exception = [['2', '!'], ['22', 'i', '!', 'M']]
        for i in test_input_correct:
            self.assertEqual(10, len(populate_string(10, i)))
        for i in test_input_exception:
            self.assertRaises(TypeError, populate_string, (10, i))

    def test_check_one_of_each_character(self):
        exception_tuple = (AssertionError, ValueError)
        test_list_correct = ['i', '2', '!', 'M']
        test_list_exception = [['i', '3'], ['ii', '3', '!', 'M'], ['i', 'm', '3', '!']]
        self.assertEqual(True, check_one_of_each_character(test_list_correct))
        for i in test_list_exception:
            self.assertRaises(exception_tuple, check_one_of_each_character, i)
