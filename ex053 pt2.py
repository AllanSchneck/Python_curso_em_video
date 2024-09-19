f = str.lower(input('Digite uma frase: ')).strip()
p = f.split()
j = ''.join(p)
i = ''
for l in range(len(j)-1, -1, -1):
    i += j[l]
if j == i:
    print('\033[32mÉ palindromo')
else:
    print('\033[31mNão é palindromo')