dados = list()
numeros = list()
pares = 0
for c in range(0,9):
    dados.append(int(input(f'Digite o valor {c}°: ')))
    numeros.append(dados[:])
    if dados[0] % 2 == 0:
        pares += dados[0]
    dados.clear()
m = numeros[3][0]
if m <= numeros[4][0]:
    m = numeros[4][0]
if m <= numeros[5][0]:
    m = numeros[5][0]
print(f'''{numeros[0]} {numeros[1]} {numeros[2]}
{numeros[3]} {numeros[4]} {numeros[5]}
{numeros[6]} {numeros[7]} {numeros[8]}''')
print(f'A soma de todos os números pares é {pares}')
print(f'A soma de todos os valores da terceira coluna é {numeros[2][0] + numeros[5][0] + numeros[8][0]} ')
print(f'O maior número da segunda fileira é {m}')
