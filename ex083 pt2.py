numeros = []
n = str(input('Digite um valor: ')).split()
ap = []
fp = []
for c in n:
    for b in c:
        numeros.append(b)
for d,v in enumerate(numeros):
    if v == '(':
        ap.append(d)
    if v == ')':
        fp.append(d)
if len(fp) == len(ap) and fp > ap:
    print('\033[32mExpressão válida')
else:
    print('\033[31mExpressão inválida')
