n = (int(input('1° Número: ')), int(input('2° Número: ')), int(input('3° Número: ')), int(input('4° Número: ')))
print(f'Os números escolhidos foram {n}')
print(f'Você digitou {n.count(9)} vezes o valor 9')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1} posição ')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
for c in n:
    if c % 2 == 0:
        print(f'Os valores pares listados são: {c}')