s = 0
for c in range(1,7):
    n = int(input('Digite o {}° valor: '.format(c)))
    n1 = (n%2)
    if n1 == 0:
        s += n
print('A soma dos números pares é igual a {}'.format(s))