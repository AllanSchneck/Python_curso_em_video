from math import radians, sin, cos, tan
a = float(input('Digite um ângulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('Esse ângulo tem:\nSeno = {:.2f}\nCosseno = {:.2f}\nTangente = {:.2f}'.format(s, c, t))
