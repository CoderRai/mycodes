import PySimpleGUI as sg

sg.theme('purple')
# informacoes exibidas na tela
layout = [[sg.Text('Digite um numero')],
          [sg.Input(key='NUMBER',size=(20,20))],
          [sg.Button('converter'),sg.Button("sair",key="sair")]]


window = sg.Window('conversor de bases numericas', layout)

while True:  # evento loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'sair':
        break
    num = int(values['NUMBER'])
    # botao de fechar

    if event == 'converter':
        sg.popup("em binário\n", bin(num)[2:],"Em Hexadecimal\n",hex(num)[2:],"Em octal\n",oct(num)[2:])
