import random
import secrets
import string

list_of_ascii_chars = ''.join(string.ascii_letters + string.punctuation + string.digits)

"""
This function generates a random combination of ascii characters to the length specified by user input.  The input
must be an integer between 4 and 20.  The output is a string of ascii characters.  
"""


def generate_password(lengthOfPassword):
    assert 3 < lengthOfPassword <= 20, "Password must be between 4 and 20 characters long"
    try:
        # Populate list with 1 of each ascii character type to ensure there is at least one of each
        password_list = [secrets.choice(string.ascii_lowercase), secrets.choice(string.ascii_uppercase),
                         secrets.choice(string.digits), secrets.choice(string.punctuation)]
        # Populate the rest of the list with random characters
        password_string = populate_string(lengthOfPassword, password_list)
        return password_string
    except ValueError:
        print("Input error: Input an integer (whole number) between 4 and 20")


"""
This function takes a valid list consisting of 4 characters (one of each - lowercase, uppercase, symbol and digit),
and an integer which defines the length of the final password.  It returns a string of user defined length.
"""


def populate_string(password_length, password_list):
    if len(password_list) != 4 or not check_one_of_each_character(password_list):
        raise ValueError("Error: The list must have 4 characters.")
    else:
        i = 4
        while i < password_length:
            character = secrets.choice(list_of_ascii_chars)
            password_list.append(character)
            i += 1
        random.shuffle(password_list)
        pass_string = ''.join(password_list)
        return pass_string


"""
This function takes input of a list of characters.  It checks that the list is equal to 4 and ensures that one of each
character type is represented.  One each of lower and uppercase, symbol and digit
"""


def check_one_of_each_character(password_list):
    lowercase = 0
    uppercase = 0
    symbol = 0
    digit = 0

    punctuation = string.punctuation

    assert len(password_list) == 4, "The list must be 4 characters long"
    for i in password_list:
        if len(i) > 1:
            raise ValueError("Error: list item is greater than one character.  Value passed is - " + i + " should be - "
                             + i[0])
        if i.isupper():
            uppercase += 1
        if i.islower():
            lowercase += 1
        if i.isdigit():
            digit += 1
        if i in punctuation:
            symbol += 1

    if lowercase and uppercase and symbol and digit == 1:
        return True
    else:
        raise ValueError("Error: There is not one of each character type.")
