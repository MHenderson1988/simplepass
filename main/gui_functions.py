import operator
import PySimpleGUI as sg
from main.classes.user import User


"""
This function takes the current window as it's argument.  It creates a new user and displays the name in the user
list.
"""


def new_user_name(aWindow, aUserList):
    user_name = sg.popup_get_text('New user name:')
    if not len(user_name) > 0:
        sg.popup_error('Username must have value!')
    else:
        updated_user_list = update_user_list(aUserList, user_name)
        names_to_display = [user.name for user in updated_user_list]
        aWindow['-USER_NAMES_LIST-'].update(names_to_display)


"""
Takes two inputs, a list of users and a name.  Returns a sorted list of instances of the User class.
"""


def update_user_list(user_list, aName):
    try:
        new_user = User(aName)
        user_list.append(new_user)
        sorted_list = sorted(user_list, key=operator.attrgetter('name'))
        return sorted_list
    except TypeError:
        print("Please enter a valid string")

