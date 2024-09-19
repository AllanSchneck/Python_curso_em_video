from random import randint
print('''\033[30;107;1mBEM VINDO AO ÍMPAR OU PAR O JOGO \033[m
\033[30;107;1mESCOLHA UM NÚMERO E TENTE GANHAR!\033[m''')
v = 0
while True:
    c = randint(0, 10)
    r = str.upper(input('ÍMPAR OU PAR? '))[0].split()
    n = int(input('Digite o Número:'))
    s = c + n
    if 'P' in r and s % 2 == 0:
        print(f'\033[32mComputador escolheu {c} você {n} a soma é {s} par, você venceu!\033[m')
        v += 1
    elif 'I' in r and s % 2 == 1:
        print(f'\033[32mComputador escolheu {c} você {n} a soma é {s} ímpar, você venceu!\033[m')
        v += 1
    else:
        break
print(f'\033[31mComputador escolheu {c} você escolheu {n} a soma é {s}, você perdeu.\033[m')
print(f'\033[34mVocê venceu {v} vezes\033[m')
