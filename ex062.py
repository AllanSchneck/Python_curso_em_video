n = int(input('Digite um número e veja sua PA: '))
r = int(input('Digite Sua razão: '))
g = 0
q = ''
while 'n' not in q:
    g += 1
    n += r
    print('\033[32;40;1m{}\033[m -> '.format(n), end='')
    if g == 10:
        q = str.lower(input('Quer continuar [S/N]? '))[0].split()
        g = 0
print('\033[34mFIM\033[m')
