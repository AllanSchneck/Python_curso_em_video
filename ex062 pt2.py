print('\033[32;40;1mPROGRAMA PHYTHON P.A.\033[m')
print('-=' * 10)
n = int(input('Digite um valor: '))
r = int(input('Digite a razão desse valor: '))
t = n
c = 1
v = 0
m = 10
while m != 0:
    v += m
    while c <= v:
        print('\033[34;40;1m{}\033[m ->'.format(t), end='')
        t += r
        c += 1
    print('PAUSA')
    m = int(input('Quantos termos você que mostrar a mais? '))
print('\033[33;40;1mfim\033[m')
