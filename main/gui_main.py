import PySimpleGUI as sg
from main.classes.users import Users


def create_main_gui():
    # Define the window's contents
    left_column = [sg.Text("-Users-"),
                   sg.Combo(key='-USER_NAMES_LIST-', size=(30,5)),
                   sg.InputText(key='-NEW_USER_NAME_TEXT-', size=(30,5)),
                   sg.Button('Add user', key='-NEW_USER_NAME_BUTTON-')]
    layout = [left_column,
              [sg.Button('Ok'), sg.Button('Quit')]]

    # Create the window
    window = sg.Window('Window Title', layout)

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        if event == 'new_user_name_button':
            user_name = values['-NEW_USER_NAME_TEXT-']
            new_user = Users(user_name)
            window.Element('user_names_list').Update(values=[new_user.name])
    # Finish up by removing from the screen
    window.close()