import math
c1 = float(input('Digite o comprimento do cateto oposto: '))
c2 = float(input('Digite o comprimento do cateto adjecente: '))
n = math.hypot(c1, c2)
print('O comprimento da hipotenusa é igual a {:.2f}'.format(n))
