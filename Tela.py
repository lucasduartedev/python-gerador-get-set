# Biblioteca para definição da interface gráfica
import PySimpleGUI as sg

# Função para retornar os Getters e Setters
def gerador(palavra):
    print('@property')
    print('def {}(self):'.format(palavra))
    print('    return self._{}'.format(palavra))
    print('')
    print('@{}.setter'.format(palavra))
    print('def {}(self, {}):'.format(palavra, palavra))
    print('    self._{} = {}'.format(palavra, palavra))

# Definição do layout
layout = [
    [   # Campo de texto para recebe a PALAVRA
        sg.Input(key='palavra', size=(15, 0)),
        # Botão para acionar a função 'geradora'
        sg.Button('GERAR', key='btn_gerar', size=(10, 0))
    ],
    [   # Campo de texto que mosta o resultado
        sg.Output(size=(30, 10))
    ],
    [   # Botão para chefar a aplicação
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

    # Palavra informada
    palavra = values['palavra']

    # Botão 'gerar' aciona a função 'geradora'
    if event in (None, 'btn_gerar'):
        gerador(palavra)

# Fechar janela
window.close()
