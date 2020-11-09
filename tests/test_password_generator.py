from unittest import TestCase
from main.password_generator import generate_password


class TestPasswordGenerator(TestCase):
    def test_generate_password(self):
        exception_tuple = (TypeError, AssertionError)
        test_input = [2, "Hello", 28382, "This is a test"]
        for i in test_input:
            self.assertRaises(exception_tuple, generate_password, i)
