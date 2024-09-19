a = int(input('Digite um ano: '))
m = (a%4) and (a%100) != 0 or a%100 == 0
if (m==0):
    print('\033[32mO ano de {} é um ano bissexto!'.format(a))
else:
    print('\033[31mO ano de {} não é bissexto'.format(a))