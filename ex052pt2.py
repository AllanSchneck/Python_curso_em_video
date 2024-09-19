n = int(input('Digite um número: '))
t = 0
for i in range(1,n + 1):
    print('{}'.format(i))
    if n % i == 0:
        print('\033[34m')
        t += 1
    else:
        print('\033[33m')
print('O número {} foi divisivel {} vezes'.format(n,t))
if t == 2:
    print('\033[32mÉ por isso que ele é primo!')
else:
    print('\033[31mPor isso ele não é primo!')
