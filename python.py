import PySimpleGUI as sg

sg.theme('reddit')

#LEYOUT
tela_login = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(password_char='*', key='senha')],
    [sg.Button('Enviar')]
]

#CRIAR JANELA

janela = sg.Window('Login',layout=tela_login)

#LER OS EVENTOS

while True:
    event, value = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Enviar':
        usuario_digitado = value['usuario']
        senha_digitada = value['senha']
        print(usuario_digitado,senha_digitada)