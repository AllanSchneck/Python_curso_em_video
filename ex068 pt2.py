from random import randint
v = 0
while True:
    j = int(input('Diga o valor: '))
    c = randint(0, 10)
    t = j + c
    e = ' '
    while e not in 'PpIi':
        e = str(input('Par ou Impar? ')).upper().strip()[0]
    print(f'Você jogou {j} e o computador {c}. Total de {t}')
    print('DEU PAR!' if t % 2 == 0 else 'DEU ÍMPAR!')
    if e == 'P':
        if t % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif e == 'I':
        if t % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
print(f'GAME OVER! Você venceu {v} vezes')
