print('\033[32;51m SEQUÊNCIA FIBONACCI\033[m')
n = int(input('Digite um número: '))
v = 0
m = n
M = 1
s = 0
while not v == 6:
    v += 1
    if n == 0 or n == 1:
        s += M
        M += s
        print('\033[31;40;1m{}\033[m -> \033[31;40;1m{}\033[m ->'.format(s, M), end='')
    elif n > 1:
        s += m
        m += s
        print(('\033[35;40;1m{}\033[m -> \033[35;40;1m{}\033[m ->'.format(s,m)), end='')
