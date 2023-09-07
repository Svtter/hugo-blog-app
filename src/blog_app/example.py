import PySimpleGUI as sg


def main():
    """use this for pysimplegui test"""
    sg.theme("DarkAmber")  # Add a touch of color
    # All the stuff inside your window.
    layout = [
        [sg.Text("New Post")],
        [sg.Text("post name:"), sg.InputText(key='-post-name-')],
        [sg.Button("Ok", key="-new-post-"), sg.Button("Cancel")],
        [sg.Button("post editor", key="-post-editor-")],
    ]

    # Create the Window
    window = sg.Window("Blog App", layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":  # if user closes window or clicks cancel
            break
        print("You entered: {values}".format(values=values))

    window.close()


if __name__ == "__main__":
    main()
