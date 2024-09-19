n = 'a'
while n not in 'FM':
        n = str.upper(input('Digite seu sexo [F/M]: ')).strip()
print('Dado resgatado com sucesso, SEXO {}.'.format(n))
