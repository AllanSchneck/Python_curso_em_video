import random
print('''BEM VINDO AO JOKENPÔ!!
COMANDOS:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
j = (int(input('Qual você escolhe pedra,papel ou tesoura? ')))
p = (0,1,2)
e = random.choice(p)
if j == 2 or 1 or 0 and e == 2 or 1 or 0:
    print('JOGADOR JOGOU {}'.format(j))
    print('computador jogou {}'.format(e))
    if j == 0 and e == 1 or j == 1 and e == 2 or j == 2 and e == 0:
        print('\033[31mCOMPUTADOR VENCE!')
    elif e == 0 and j == 1 or e == 1 and j == 2 or e == 2 and j == 0:
        print('\033[32mJOGADOR VENCE')
    elif j == e:
        print('\033[33mEMPATE!')
    else:
        print('\033[31mJOGADA INVÁLIDA')
else:
    print('\033[31mJOGADA INVÁLIDA!')