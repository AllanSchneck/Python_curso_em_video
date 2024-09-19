
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
    return F'R${msg:.2f}'.replace('.', ',')
