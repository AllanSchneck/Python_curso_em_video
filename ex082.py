numeros = list()
pares = list()
impares = list()
while True:
    numeros.append(int(input('Digite um valor: ')))
    if numeros[-1] % 2 == 0:
        pares.append(numeros[-1])
    else:
        impares.append(numeros[-1])
    r = str.upper(input('Quer continuar [S/N]? ')).strip()[0]
    if 'N' in r:
        break
print(f'Os números escolhidos foram {numeros}')
print(f'Os números pares são {pares}')
print(f'Os números ímpares são {impares}')
