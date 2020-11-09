import secrets
import random
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
        # Set counter to 4 to accommodate for the 4 characters already created
        i = 4
        while i < lengthOfPassword:
            character = secrets.choice(list_of_ascii_chars)
            password_list.append(character)
            i += 1
        random.shuffle(password_list)
        pass_string = ''.join(password_list)
        return pass_string
    except ValueError:
        print("Input error: Input an integer (whole number) between 4 and 20")
