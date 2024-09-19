v = t = m = c = s = 0
b = ''
while True:
    c += 1
    p = str.lower(input('Digite o nome do produto: '))
    v = float(input('PREÇO:R$ '))
    t += v
    if v >= 1000:
        m += 1
    if c == 1 or v < s:
        s = v
        b = p
    r = str.lower(input('Quer continuar [S/N]? '))[0].split()
    if 'n' in r:
        break
print(f'O valor de todos os produtos somados é {t}')
print(f'O produto mais barato é {b} que custa R${s}')
print(f'{m} produtos custam mais que R$1.000')
