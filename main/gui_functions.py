import operator
import PySimpleGUI as sg
from main.classes.user import User


"""
This function takes the current window as it's argument.  It creates a new user and displays the name in the user
list.
"""


def new_user_name(aUserList):
    user_name = sg.popup_get_text('New user name:')
    if not len(user_name) > 0:
        sg.popup_error('Username must have value!')
    else:
        return update_user_list(aUserList, user_name)


"""
Takes two inputs, a list of users and a name.  Returns a sorted list of instances of the User class.
"""


def update_user_list(user_list, aName):
    try:
        new_user = User(aName)
        user_list.append(new_user)
        user_list.sort(key=operator.attrgetter('name'))
        return user_list
    except TypeError:
        print("Please enter a valid string")

