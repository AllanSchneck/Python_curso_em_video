numeros = list()
posM = list()
posm = list()
for c in range(0,5):
    numeros.append(int(input('Digite um número: ')))
for v,n in enumerate(numeros):
    if max(numeros) == n:
        posM.append(v)
    if min(numeros) == n:
        posm.append(v)
print(f'Os números selecionados foram {numeros}')
print(f'O menor valor digitado foi {min(numeros)} nas posições {posm}')
print(f'O Maior valor digitado foi {max(numeros)} nas posições {posM} ')
