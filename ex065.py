q = ''
v = m = M = s = n = 0
print('Calculador de média Python ')
while not q == 'n':
    v += 1
    n = int(input('Digite um número inteiro: '))
    s += n
    if v == 1:
        M = m = n
    if n > M:
        M = n
    if n < m:
        m = n
    if v:
        q = str.lower(input('Quer continuar?[S/N]: ')).strip()[0]
print('Somando os valores digitados a média será {}'.format(s/v))
print('O maior número lido é {} e o menor {}'.format(M, m))
