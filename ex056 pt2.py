mi = 0
z = 'Não a homens no grupo'
v = 0
h = 0
for c in range(1,5):
    i = int(input('Idade: '))
    s = str.lower(input('Sexo [M/F]: '))
    n = str.upper(input('Nome: '))
    if c:
        if s == 'feminino' or 'f' == True:
            if i < 20:
                v += 1
    if c == 1 and s in 'm':
        h = i
        z = n
    if s in 'm' and i > h:
        h = i
        z = n
print('A média idade do grupo é de {} anos'.format(mi))
print('O nome do homem mais velho do grupo é ({})'.format(z))
print('O grupo contém {} mulheres com menos de 20 anos'.format(v))