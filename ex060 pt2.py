n = int(input('Digite um número: '))
g = n+1
f = 1
while not 1 == g:
    g -= 1
    f *= g
    print(g)
print('{}! = {}'.format(n, f))
