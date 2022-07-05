#aqui a gente vai usar o pysimplegui, para ter certeza que você tem ele instalado, execute pip install pysimplegui no terminal do python
import PySimpleGUI as sg

layout = [
    [sg.Text('Calculadora de 2 números inteiros')],
    [sg.Text("Primeiro Número"),sg.InputText(key='primeironumero')],
    [sg.Text("Segundo Número"),sg.InputText(key='segundonumero')],
    [sg.Button('Somar')],
    [sg.Text(key='textofinal')]
]
janela = sg.Window('Calculadora',layout)
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Somar':
        primeiro_valor = (valores["primeironumero"])
        segundo_valor = (valores["segundonumero"])
        
        janela['textofinal'].update(f'A soma entre {primeiro_valor} e {segundo_valor} é {primeiro_valor+segundo_valor}')

janela.close