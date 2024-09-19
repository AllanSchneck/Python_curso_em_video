
def metade(n=0, g=False):
    if g:
        return f'R${n / 2}'
    else:
        return n / 2


def diminuir(n=0, p=0, g=False):
    if g:
        return f'R${n - ((n/100) * p)}'
    else:
        return n - ((n/100) * p)


def dobro(n=0, g=False):
    if g:
        return f'R${n * 2}'
    else:
        return n * 2


def aumentar(n=0, p=0, g=False):
    if g:
        return f'R${n + ((n/100) * p)}'
    else:
        return n + ((n/100) * p)


def moeda(msg):
    return f'R${msg}'


def resumo(n=0, p=0, p1=0):
    print('-' * 40)
    print('         RESUMO DO VALOR')
    print('-' * 40)
    print(f'''Preço analisado:    R${n}
Dobro do preço:     R${n * 2}
Metade do preço     R${n / 2}
{p}% de aumento:     R${n + ((n/100)* p)}
{p1}% de redução      R${n - ((n/100) * p1)}''')
    print('-' * 40)
