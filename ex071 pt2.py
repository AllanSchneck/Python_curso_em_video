print('-=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('-=' * 30)
v = int(input('Que valor você quer sacar? R$'))
t = v
c = 50
tc = 0
while True:
    if t >= c:
        t -= c
        tc += 1
    else:
        if tc > 0:
            print(f'Total de {tc} Cédulas de R${c}')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        tc = 0
        if t == 0:
            break
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
