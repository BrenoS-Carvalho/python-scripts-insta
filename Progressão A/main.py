print('-------PROGRESSÃO ARITMÉTRICA -----')
contador = 1
primeiro_termo = int(input('Qual o primeiro termo da pa: '))
razao = int(input('Qual a razão da pa: '))
numero_de_termos = int(input('Qual a quantidade de termos que você deseja: '))
print('Progressão')
print('='*30)
print(primeiro_termo, end=' ')
while contador < numero_de_termos:
    print(razao + primeiro_termo, end=' ')
    primeiro_termo = razao + primeiro_termo
    contador += 1
print(f'\nO {numero_de_termos}° número dessa progressão aritmétrica é {primeiro_termo}.')
