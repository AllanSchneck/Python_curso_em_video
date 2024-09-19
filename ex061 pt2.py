print('Gerador de PA')
print('-=' * 10)
n = int(input('Primeiro Termo: '))
r = int(input('Digite su razão'))
t = n
c = 1
while c <= 10:
    print('{} --> '.format(t), end='')
    t += r
    c += 1
