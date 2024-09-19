n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Convereter para HEXAGONAL)''')
o = int(input('Sua opção: '))
if o == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n,bin(n)))
    print('{} convertido para BINÁRIO é igual a {}'.format(n,bin(n)[2:]))
elif o == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n,oct(n)[2:]))
elif o == 3:
    print('{} convertido para HEXADECIMAL é igual {}'.format(n,hex(n)[2:]))
else:
    print('OPÇÃO INVÁLIDA!')