dados = list()
numeros = list()
impares = list()
pares = list()
i = 0
for c in range(1,8):
    dados.append(int(input(f'Digite o {c}° valor: ')))
    if dados[0] % 2 == 0:
        numeros.append(dados[:])
    else:
        numeros.insert(0, dados[:])
    dados.clear()
for v,n in enumerate(numeros):
    if n[0] % 2 != 0:
        i = v
pares.append(numeros[i+1:])
pares[0].sort()
impares.append(numeros[0:i+1])
impares[0].sort()
print(f'Os números pares e impares dentro da mesma lista ficam {numeros}')
print(f'Os números pares são {pares[0]}')
print(f'Os numeros ímpares são {impares[0]}')
