n = 0
s = 0
b = 0
print('QUANDO QUISER PARAR DIGITE 999')
while not n == 999:
    n = int(input('DIGITE QUALQUER VALOR: '))
    s += n
    b += 1
print('A SOMA DOS VALORES DIGITADOS É IGUAL A {}'.format(s-999))
print('Foram digitados {} números'.format(b-1))
