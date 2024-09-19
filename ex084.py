pessoas = list()
dados = list()
pesos = []
m = []
g = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    r = str.lower(input('Quer continuar [S/N]? '))
    if 'n' in r:
        break
for p in pessoas:
    if p[1]:
        pesos.append(p[1])
for v,c in enumerate(pesos):
    if max(pesos) == c:
        g.append(pessoas[v][0])
    if min(pesos) == c:
        m.append(pessoas[v][0])
print(f'Temos um total de {len(pessoas)} cadastrados')
print(f'As pessoas mais leves são {m}')
print(f'As pessoas mais pesadas são {g}')
