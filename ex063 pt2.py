print('-=' * 10)
print('SEQUÊNCIA DE FIBONACCI')
print('=-' * 10)
n = int(input('Quantos termos você quer mostrar?'))
t = 0
t1 = 1
print('~' * 30)
print('{} -> {}'.format(t, t1), end='')
c = 3
while c <= n:
    t2 = t+t1
    t = t1
    t1 = t2
    print('. -> {}'.format(t2), end=' ')
    c += 1
print(' fim')
