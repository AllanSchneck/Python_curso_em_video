numeros = list()
while True:
    numeros.append(int(input('Digite um valor: ')))
    r = str.upper(input('Quer continuar [S/N]? ')).split()[0]
    if 'N' in r:
        break
numeros.sort(reverse=True)
print(f'Foram digitados {len(numeros)} números')
print(f'A lista em ordem decrescente ficará: {numeros}')
if 5 in numeros:
    print('O numero 5 foi digitado e está na lista')
else:
    print('O número 5 não foi digitado! e não está na lista')
