
def metade(n=0, g=False):
    if g:
        return f'{moeda(n / 2)}'
    else:
        return n / 2


def diminuir(n=0, p=0, g=False):
    if g:
        return f'{moeda(n - ((n/100) * p))}'
    else:
        return n - ((n/100) * p)


def dobro(n=0, g=False):
    if g:
        return f'{moeda(n * 2)}'
    else:
        return n * 2


def aumentar(n=0, p=0, g=False):
    if g:
        return f'{moeda(n + ((n/100) * p))}'
    else:
        return n + ((n/100) * p)


def moeda(msg):
    return f'R${msg:.2f}'.replace('.', ',')


def resumo(n=0, p=0, p1=0):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f'''Preço analisado:    {moeda(n)}
Dobro do preço:     {moeda(n * 2)}
Metade do preço     {moeda(n / 2)}
{p}% de aumento:     {moeda(n + ((n/100)* p))}
{p1}% de redução      {moeda(n - ((n/100) * p1))}''')
    print('-' * 40)
