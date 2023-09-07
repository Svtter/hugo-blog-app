import PySimpleGUI as sg
from blog_app.editor import open_post_editor, new_post


def main():
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
        if event == "-new-post-":
            new_post(values['-post-name-'])
        elif event == '-post-editor-':
            open_post_editor()
        if event == sg.WIN_CLOSED or event == "Cancel":  # if user closes window or clicks cancel
            break

    window.close()


if __name__ == "__main__":
    main()

