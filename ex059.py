sp = 0
print('\033[33;40mSELECIONE DOIS NÚMEROS')
n1 = int(input('Digite um valor: '))
n = int(input('Digite outro valor: \033[m'))
while not sp == 5:
    sp = int(input('''\033[;40m[1] PARA MULTIPLICAR
[2] SOMAR
[3] DESCOBRIR O MAIOR
[4] ESCOLHER NOVOS NÚMEROS
[5] SAIR
Digite: \033[m'''))
    if sp == 1:
        print('\033[35mA multiplicação de {} e {} é {}\033[m'.format(n, n1, n*n1))
    if sp == 2:
        print('\033[36mA soma entre {} e {} é igual a {}\033[m'.format(n, n1, n+n1))
    if sp == 3:
        if n == n1:
            print('\033[34mNão existe maior ambos são iguais {} e {}\033[m'.format(n1, n))
        elif n > n1:
            print('\033[33m{} é maior que {}\033[m'.format(n, n1))
        else:
            print('\033[;40m{} é maior que {}\033[m'.format(n1, n))
    if sp == 4:
        n1 = int(input('Digite um valor: '))
        n = int(input('Digite outro valor: '))
    if sp > 5:
        print('\033[31;40mOpção inválida!\033[m')
print('\033[30;45;1mFIM\033[m')
