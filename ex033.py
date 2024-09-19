a = int(input(' um número: '))
b = int(input(' o segundo número: '))
c = int(input(' terceiro número: '))
m = a
if b<c and b<a:
    m = b
if c<b and c<a:
    m = c
M = a
if b>a and b>c:
    M = b
if c>a and c>b:
    M=c
print('\033[1;30;107mO menor valor digitado foi {}\033[m'.format(m))
print('\033[1;30;43mO maior valor digitado foi {}\033[m'.format(M))