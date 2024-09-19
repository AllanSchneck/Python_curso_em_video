numeros = list()
while True:
    n = int(input('Digite um valor: '))
    resp = str.upper(input('Quer continuar [S/N]: ')).strip()[0]
    while resp not in 'SN':
        resp = str.upper(input('Quer continuar [S/N]')).strip()[0]
    numeros.append(n)
    if 'N' in resp:
        break


def maior(lst):
    print('-' * 30)
    print('Analisando os valores passados....')
    print(f'Foram passados {len(lst)} valores que são {lst}')
    print(f'O maior valor digitado é {max(lst)}')
    print('-' * 30)


maior(numeros)
