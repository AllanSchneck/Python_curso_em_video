n = int(input('digite um número: '))
r = (n%2)
if (r==0):
    print('Seu número é \033[32m{}\033[m par'.format(n))
else:
    print('Seu número é \033[31m{}\033[m ímpar '.format(n))
