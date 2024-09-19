import math
c1 = float(input('Digite o comprimento do cateto oposto de um triângulo retângulo: '))
c2 = float(input('Agora o comprimento do cateto adjecente do mesmo: '))
n1 = math.pow(c1, 2)
n2 = math.pow(c2, 2)
h = math.sqrt(n1+n2)
print('O comprimento da hipotenusa desse triângulo retângulo é igual a \033[1;30;41m{:.2f}\033[m'.format(h))
