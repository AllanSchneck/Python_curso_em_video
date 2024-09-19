mi = 0
z = 0
v = 0
h = 0
q = ''
for c in range(1, 5):
    i = int(input('Idade: '))
    s = str.lower(input('Sexo [F/M]: '))
    n = str.upper(input('Nome: '))
    mi += i/4
    if c == 1 and s in 'm':
        q = n
        h = i
    if s in 'm' and i > h:
        h = i
        q = n
    if s in 'f' and i < 20:
        v += 1

print('O nome do homem mais velho do grupo é {} com {} anos'.format(q,h))
print('o grupo contém {} mulheres com menos de 20 anos'.format(v))
print('A média idade do grupo é de {} anos'.format(mi))
