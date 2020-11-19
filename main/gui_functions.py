from main.classes.user import User


def update_user_list(user_list, aName):
    try:
        new_user = User(aName)
        user_list.append(new_user)
        to_display = [user.name for user in user_list]
        return user_list, to_display
    except TypeError:
        print("Please enter a valid string")

