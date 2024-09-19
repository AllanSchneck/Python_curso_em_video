s = q = 0
print('Digite quatro números!')
n = (int(input('1° Número: ')), int(input('2° Número: ')), int(input('3° Número: ')), int(input('4° Número: ')))
print(f'\033[36;1;40mOs números escolhidos foram {n}\033[m')
print('\033[34;1;40mOs números pares são:\033[m', end='')
for i in n:
    if i % 2 == 0:
        print(f'\033[34;1;40m{i}\033[m', end=' ')
    if i == 9:
        s += 1
    if i == 3:
        q = 3
if s >= 1:
    print(f'\n\033[31;1;40mO número 9 apareceu {s} vezes\033[m')
else:
    print('\n\033[31mO número 9 não apareceu!\033[m')
if q == 3:
    print(f'Primeira vez que {q} aparece é na {n.index(3)+1}° posição')
else:
    print('Não foi digitado nenhum 3')

