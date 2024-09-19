i = v = h = m = 0
s = ''
while True:
    while 'fm' not in s:
        s = str.lower(input('Digite seu sexo [F/M]: '))[0].split()
        if 'f' in s or 'm' in s:
            break
    i = int(input('Digite sua idade: '))
    if i >= 18:
        v += 1
    if 'm' in s:
        h += 1
    elif 'f' in s and i <= 20:
        m += 1
    print('Cadastro confirmado.')
    r = str.upper(input('Quer continuar [S/N]? '))[0].split()
    if 'N' in r:
        break
print(f'{v} pessoas tem mais de 18 anos.')
print(f'{h} homens foram cadastrados.')
print(f'{m} mulheres tem menos de 20 anos')
