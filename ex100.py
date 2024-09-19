from random import randint
from time import sleep
numeros = list()


def sorteio():
    print('Sorteando 5 valores: ',end=' ',flush=True)
    for c in range(1,6):
        n = randint(0,10)
        numeros.append(n)
        print(f'{n}',end=' ',flush=True)
        sleep(0.5)
    print('PRONTO')


def somapar(lst):
    s = 0
    for l in lst:
        if l % 2 == 0:
            s += l
    print(f'Somando os valores pares de {lst}, temos {s}')


sorteio()
somapar(numeros)
