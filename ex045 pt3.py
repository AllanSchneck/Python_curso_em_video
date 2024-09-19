from random import randint
i = ('Pedra','Papel','Tesoura')
c = randint(0, 2)
print('''Sua opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
j = int(input('Qual sua jogada? '))
print('-=' * 11)
print('Computador jogou {}'.format(i[c]))
print('Jogador jogou {}'.format(i[j]))
print('-=' * 11)
if c == 0:
    if j == 0:
        print('\033[33mEMPATE!')
    elif j == 1:
        print('\033[32mJOGADOR VENCE!')
    elif j == 2:
        print('\033[31mCOMPUTADOR VENCE!')
    else:
        print('\033[31mJOGADA INVÁLIDA!')
elif c == 1:
    if j == 0:
        print('\033[31mCOMPUTADOR VENCE!')
    elif j == 1:
        print('\033[33mEMPATE!')
    elif j == 2:
        print('\033[32mJOGADOR VENCE!')
    else:
        print('\033[31mJOGADA INVÁLIDA')
elif c == 2:
    if j == 0:
        print('\033[32mJOGADOR VENCE!')
    elif j == 1:
        print('\033[31mCOMPUTAOR VENCE!')
    elif j == 2:
        print('\033[33mEMPATE!')
    else:
        print('\033[31mJOGADA INVÀLIDA')
else:
    print('\033[31mJOGADA INVÁLIDA')