n = int(input('Digite seu número: '))
f = 1
for i in range(n, 0, -1):
    f *= i
print('{}! = {}'.format(n, f))
