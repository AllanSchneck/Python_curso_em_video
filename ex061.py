n = int(input('Digite um valor de descubra sua PA: '))
r = int(input('Digite sua razão: '))
g = 0
while not g == 10:
    g += 1
    n += r
    print('{} -> '.format(n),end= '')
print('FIM')
