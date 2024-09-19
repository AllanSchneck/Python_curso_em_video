import math
a = float(input('Digite um ângulo: '))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
s = math.sin(math.radians(a))
print('Seno \033[32m{}\033[m\ncosseno\033[34m{}\033[m\ntangente\033[36m{}\033[m'.format(s, c, t))
