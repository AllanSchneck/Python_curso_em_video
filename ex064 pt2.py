s = b = 0
print('QUANDO QUISER PARAR DIGITE 999')
n = int(input('DIGITE QUALQUER VALOR: '))
while not n == 999:
    s += n
    b += 1
    n = int(input('DIGITE QUALQUER VALOR: '))
print('FORMA DIGITADOS {} VALORES E A SOMA ENTRE ELES É IGUAL A {}'.format(b, s))
