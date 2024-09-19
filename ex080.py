numeros = list()
n = 0
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > max(numeros):
        numeros.append(n)
    else:
        pos = 0
        while pos <= len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                break
            pos += 1
print(f'Os números em ordem crescente ficará {numeros}')
