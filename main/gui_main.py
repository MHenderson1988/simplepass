import PySimpleGUI as sg
from main.gui_functions import new_user_name

user_list = []


def create_main_gui():
    # Define the window's contents
    left_column = [[sg.Text("-Users-")],
                   [sg.Listbox(values=[], key='-USER_NAMES_LIST-', size=(30, 6), enable_events=True)],
                   [sg.Button('Add', key='-NEW_USER_NAME_BUTTON-')],
                   [sg.Button('Edit', key='-EDIT_USER_NAME_BUTTON-')],
                   [sg.Button('Delete', key='-DELETE_USER_NAME_BUTTON-')]]

    right_column = [[sg.Text("-Websites and passwords-")],
                    [sg.Listbox(values=[], key='-WEBSITES-AND-PASSWORDS-', size=(30, 6))],
                    [sg.Button('Add', key='-ADD_WEBSITE_BUTTON-')],
                    [sg.Button('Edit', key='-EDIT_WEBSITE_BUTTON-')],
                    [sg.Button('Remove', key='-REMOVE_WEBSITE_BUTTON-')]]

    layout = [[sg.Column(left_column), sg.Column(right_column)]]

    # Create the window
    window = sg.Window('Window Title', layout)

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        if event == '-NEW_USER_NAME_BUTTON-':
            new_user_name(user_list)
            window['-USER_NAMES_LIST-'].update(user.name for user in user_list)
    # Finish up by removing from the screen
    window.close()
