import math
t = int(input('Digite o primeiro termo de uma P.A. :'))
r = int(input('Digite sua razão: '))
c = math.nextafter(t,r)
print('1° termo: {}'.format(t))
for i in range(2,11):
    c += r
    print('{}° termo: {:.1f}'.format(i,c))