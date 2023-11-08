import PySimpleGUI as sg

sg.theme('DarkAmber')

def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    if imc < 17:
        categoria = 'Muito abaixo do peso'
    elif 17 <= imc < 18.5:
        categoria = 'Abaixo do peso'
    elif 18.5 <= imc < 25:
        categoria = 'Peso normal'
    elif 25 <= imc < 30:
        categoria = 'Acima do peso'
    elif 30 <= imc < 35:
        categoria = 'Obesidade I'
    elif 35 <= imc < 40:
        categoria = 'Obesidade II (severa)'
    else:
        categoria = 'Obesidade III (mórbida)'
    return imc, categoria

layout = [
    [sg.Text('Nome do Paciente: '), sg.InputText(key='nome')],
    [sg.Text('Endereço Completo:'), sg.InputText(key='endereco')],
    [sg.Text('Altura (m):'), sg.InputText(key='altura')],
    [sg.Text('Peso (kg):'), sg.InputText(key='peso')],
    [sg.Multiline('Resultado', size=(30, 5), key='resultado')],
    [sg.Button('Calcular'), sg.Button('Reiniciar'), sg.Button('Sair')]
]

window = sg.Window('Calculo do IMC - Índice de Massa Corporal', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break

    if event == 'Reiniciar':
        window['nome'].update('')
        window['endereco'].update('')
        window['altura'].update('')
        window['peso'].update('')
        window['resultado'].update('')

    if event == 'Calcular':
        nome = values['nome']
        endereco = values['endereco']
        altura = float(values['altura'])
        peso = float(values['peso'])

        imc, categoria = calcular_imc(peso, altura)
        resultado = f'Nome: {nome}\nEndereço: {endereco}\nIMC: {imc:.2f}\nResultado: {categoria}'
        window['resultado'].update(resultado)

window.close()