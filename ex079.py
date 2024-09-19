numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n in numeros:
        print('\033[31mValor duplicado, não será adicionado\033[m')
    else:
        numeros.append(n)
        print('\033[32mValor adicionado\033[m')
    r = str.upper(input('\033[33mQuer continuar [S/N]? \033[m')).strip()[0]
    if 'N' in r:
        numeros.sort()
        break
print(f'Os valores digitados em ordem crescente foram {numeros}')
