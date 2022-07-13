import pwnedpasswords as lp
import PySimpleGUI as sg


THEME_WINDOW = "DarkRed1"

class pwned_gui:

    def __init__(self, theme):
        self.theme = theme
        sg.theme(self.theme)

    def win_pwnedpassword(self):
        layout = [
            [sg.Text('Type your password in here', size=(20,1))],
            [sg.InputText(do_not_clear=False,key='-IN-')],
            [sg.Text('',justification="left", key='-OUT-')],
            [sg.Button('Check'), sg.Button('Cancel')]
        ]
        window = sg.Window('Pwnedpassword', layout)
        while True:
            event, values = window.read()
            def check_pwned():
                check=lp.check(values['-IN-'])
                if (int(check) == 0):
                    return "Kata sandi Anda tidak muncul di basis data kata sandi yang bocor"
                else:
                    return f"Kata sandi ini muncul {check} kali dalam database kata sandi yang bocor"

            if event in (None, 'Cancel'):
                break
            if event == 'Check':
                window['-OUT-'].update(check_pwned())

        window.close()

main = pwned_gui(THEME_WINDOW)
main.win_pwnedpassword()