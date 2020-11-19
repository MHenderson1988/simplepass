import operator
from main.classes.user import User


def update_user_list(user_list, aName):
    try:
        new_user = User(aName)
        user_list.append(new_user)
        sorted_list = sorted(user_list, key=operator.attrgetter('name'))
        return sorted_list
    except TypeError:
        print("Please enter a valid string")

