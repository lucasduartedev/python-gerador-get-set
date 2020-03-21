import PySimpleGUI as sg

# Definição do layout
layout = [
    [
        sg.Input(key='palavra', size=(15, 0)),
        sg.Button('GERAR', key='btn_gerar', size=(10, 0))
    ],
    [
        sg.Output(size=(30, 20))
    ],
    [
        sg.Button('FECHAR', key='btn_fechar', size=(10, 0))
    ]
]

# Criar janela
window = sg.Window('Gerador' ,layout)

# Laço para manter janela aberta
while True:
    event, values = window.read()

    # Fechar programa após clicar em 'Cancelar'
    if event in (None, 'btn_fechar'):
        break

    if event in (None, 'btn_gerar'):
        print('Teste')

    # Pegar palavra
    palavra = values['palavra']

# Fechar janela
window.close()
