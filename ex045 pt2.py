import random
print('''\033[1;30;41m[BEM VINDO AO JOKENPÔ OU FAMOSO PEDRA, PAPEL, TESOURA]\033[m''')
j = str(input('AGORA ESCOLHA PEDRA, PAPEL OU TESOURA? '))
j1 = j.upper()
p = ('PEDRA','PAPEL','TESOURA')
c = random.choice(p)
if j1 == 'PEDRA' or 'TESOURA' or 'PAPEL' and c == 'PEDRA' or 'TESOURA' or 'PAPEL':
    print('COMPUTADOR JOGOU {}'.format(c))
    print('JOGADOR JOGOU {}'.format(j1))
    if c == 'PEDRA' and j1 == 'PAPEL' or c == 'PAPEL' and j1 == 'TESOURA' or c == 'TESOURA' and j1 == 'PEDRA':
        print('\033[32;40mJOGADOR VENCE\033[m')
    elif j1 == 'PEDRA' and c == 'PAPEL' or j1 == 'PAPEL' and c == 'TESOURA' or j1 == 'TESOURA' and c == 'PEDRA':
        print('\033[31;40mCOMPUTADOR VENCE\033[m')
    elif j1 == c:
        print('\033[33;40mEMPATE!\033[m')
    else:
        print('\033[31mJOGADA INVÁLIDA!')
else:
    print('\033[31mJOGADA INVÁLIDA!')