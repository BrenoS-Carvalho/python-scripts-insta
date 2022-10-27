def fatorial(n):
    fatorial = 1
    contador = n
    while contador >= 1:
        fatorial = fatorial * contador
        contador = contador - 1
    return fatorial
print('='*10)
print(fatorial(5))
print(fatorial(4))
print(fatorial(3))
print(fatorial(10))
print('='*30)
