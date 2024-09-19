num = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        num[1].append(valor)
    else:
        num[0].append(valor)
num[1].sort()
num[0].sort()
print('-=' * 30)
print(f'Todos os valores: {num}')
print(f'Os valores pares digtados foram: {num[1]}')
print(f'Os valores impares digitados foram: {num [0]}')
