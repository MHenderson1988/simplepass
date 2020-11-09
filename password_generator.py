from datetime import datetime
from array import array

import random
import string

lower_case = []
upper_case = []
numbers = []
symbols = []


for i in string.ascii_lowercase:
    lower_case.append(i)

for i in string.ascii_uppercase:
    upper_case.append(i)

for i in string.printable[0:10]:
    numbers.append(i)

for i in string.printable[62:94]:
    symbols.append(i)


def random_lower_case():
    return random.choice(lower_case)


def random_upper_case():
    return random.choice(upper_case)


def random_number():
    return random.choice(numbers)


def random_symbol():
    return random.choice(symbols)

function_list = [random_upper_case(), random_lower_case(), random_symbol(), random_number()]


"""
This function ensures that there is at least one uppercase, lowercase, symbol and digit in the password.
Takes no input and returns a list with the ascii characters
"""


def minimum_one_each_type():
    char_list = [random_upper_case(), random_lower_case(), random_symbol(), random_number()]
    return char_list

"""
This function populates a list which already has one of each ascii character type.  It takes a number greater than 3 
and equal or less than 20 as it's input and outputs a string to the specified length
"""


def generate_password(lengthOfPassword):
    assert 3 < lengthOfPassword <= 20, "Password must be between 4 and 20 characters long"
    password_list = minimum_one_each_type()
    i = 0
    while i < lengthOfPassword:
        character = function_list[random.randint(0,3)]
        password_list.append(character)
        i += 1
    random.shuffle(password_list)
    pass_string = ''.join(password_list)
    return pass_string