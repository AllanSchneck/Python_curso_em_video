p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p+(10-1)*r
for c in range(p,d,r):
    print('{}° Termo'.format(c))