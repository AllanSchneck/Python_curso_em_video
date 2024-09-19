s = 0
for c in range(0,500+1):
    d = (c%2)
    if d == 1:
        t = (c%3)
        if t == 0:
            s += c
print('A soma de todos os valores é de {}'.format(s))
