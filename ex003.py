n = int(input('Digite um número: '))
n1 = int(input('Digite mais um número: '))
s = (n+n1)
c = {'amarelo': '\033[33m', 'azul': '\033[34m', 'roxo': '\033[35m', 'limpa': '\033[m'}
print('A soma de {}{}{} e {}{}\033[m resulta em {}{}'.format(c['amarelo'], n, c['limpa'], c['azul'], n1, c['roxo'], s))
