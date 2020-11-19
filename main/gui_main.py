import PySimpleGUI as sg
from main.gui_functions import update_user_list

user_list = []


def create_main_gui():
    # Define the window's contents
    left_column = [[sg.Text("-Users-")],
                   [sg.Listbox(values=[], key='-USER_NAMES_LIST-', size=(30, 6))],
                   [sg.InputText(key='-NEW_USER_NAME_TEXT-', size=(30, 4))],
                   [sg.Button('Add user', key='-NEW_USER_NAME_BUTTON-')]]

    right_column = [[sg.Text("-Websites and passwords-")],
                    [sg.Listbox(values=[], key='-WEBSITES-AND-PASSWORDS', size=(30, 6))],
                    [sg.InputText(key='-A_WEBSITE_NAME', size=(30, 4))],
                    [sg.Button('Generate Password', key='-PASSWORD_GENERATE_BUTTON')]]

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
            if not len(values['-NEW_USER_NAME_TEXT-']) > 0:
                sg.popup_error('Username must have value!')
            else:
                updated_user_list = update_user_list(user_list, values['-NEW_USER_NAME_TEXT-'])
                names_to_display = [user.name for user in updated_user_list]
                window['-USER_NAMES_LIST-'].update(names_to_display)
                window['-NEW_USER_NAME_TEXT-'].update('')

    # Finish up by removing from the screen
    window.close()
