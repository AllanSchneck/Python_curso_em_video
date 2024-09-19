v = 16
q = y = s = 0
g = ''
Futebol = ('Botafogo', 'Palmeiras', 'São Paulo', 'Atlético-MG', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Fluminense',
           'Fortaleza', 'Bragantina', 'Athletico-PR', 'Santos', 'Internacional', 'Corinthians', 'Cuiabá', 'Bahia',
           'Goiàs', 'Vasco da Gama', 'América-MG', 'Curitiba')
print(f'\033[30;1;107mTabela do Brasileirão\033[m')
for c in Futebol:
    y += 1
    if 'Internacional' in c:
        s = y
        g = c
    print(f'{y}° {c}')
print('\033[32;1;40mOs 5 primeiros colocados são:\033[m')
for p in Futebol[0:5]:
    q += 1
    print(f'{q}° {p}')
print('\033[31;1;40mOs 4 últimos colocados são:\033[m')
for u in Futebol[-4:]:
    v += 1
    print(f'{v}° {u}')
alfa = sorted(Futebol)
print('\033[34;1;107mTodos os Times em ordem alfábetica\033[m')
for a in alfa:
    print(a)
if 'Internacional' == g:
    print(f'{g} está na colocação {s}°')
else:
    print('\033[31mInternacinal não encontrado(a) na Tabela!\033[m')
