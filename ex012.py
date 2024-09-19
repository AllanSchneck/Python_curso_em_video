P = int(input('Digite o valor do produto: '))
d = (P-(P/100*5))
print('Sendo valor antigo \033[1;32mR${}\033[m com desonto de 5% ficará em torno de \033[1;32mR${}\033[m'.format(P, d))
