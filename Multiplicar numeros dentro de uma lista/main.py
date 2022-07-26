lista = []
contador = 1
multiplicacao = 1
while True: 
    numero = input(f'Digite o {contador}° número: ')
    if numero == 'breno.codes':
        break
    numero = int(numero)
    lista.append(numero)
    multiplicacao = multiplicacao * numero
    contador = contador + 1
print(f'Você digitou os números {sorted(lista)}')
print(f'O produto entre eles é {multiplicacao}')
