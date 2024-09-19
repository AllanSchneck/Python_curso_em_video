f = str.lower(input('Digite uma frase: ')).strip()
r = f.split()
v = ''.join(r)
s = len(v)
h = 0
for c in range(0,s+1):
    j = (v[c+1::-1])
    k = (v[:c:])
    if j == k:
        h += 1
if h == +1:
    print('\033[32mÉ um palindromo')
else:
    print('\033[31mNão é palindromo')