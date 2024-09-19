from random import randint
v = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
s = m = M = 0
for c in v:
    s += 1
    if s == 1:
        m = c
        M = c
    else:
        if c < m:
            m = c
        if c > M:
            M = c
print(f'Os números aleatórios foram {v}')
print(f'O Maior número é {M}')
print(f'O Menor número é {m}')
