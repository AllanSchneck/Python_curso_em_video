from datetime import datetime
v = datetime.now()
i = v.year
s = 0
p = 0
for c in range(0, 7):
    d = int(input('Digite seu ano de nascimento: '))
    if i-d >= 21:
        s += 1
    else:
        p += 1
print('{} pessoas já atingiram maioridade'.format(s))
print('{} pessoas não atingiram a maioridade'.format(p))
