import PySimpleGUI as sg

sg.theme('purple')
# informações exibidas na tela
layout = [[sg.Text('Digite um número')],
          [sg.Input(key='NUMBER')],
          [sg.Button('converter')],
          [sg.Output(size=(30, 15)), sg.Button('sair', size=(5, 5))]]

window = sg.Window('conversor de bases númericas', layout)

while True:  # evento loop
    event, values = window.read()

    num = int(values['NUMBER'])
    # botão de fechar
    if event == sg.WIN_CLOSED or event == 'sair':
        break
    if event == 'converter':
        print('Em binario o N° {} é:\n {}\n'.format(num, bin(num)[2:]))
        print('Em hexadecimal o N° {} é:\n {}\n'.format(num, hex(num)[2:]))
        print('Em octal o N° {} é:\n {}\n'.format(num, oct(num)[2:]))
