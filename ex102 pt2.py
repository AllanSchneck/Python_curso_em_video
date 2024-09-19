def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número
    :prompt n: O número a ser calculado
    :prompt show: (opcional) Mostrar ou não a conta
    :return: O valor fatorial de um número

    Parameters
    ----------
    n
    show

    Returns
    -------

    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ',end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=False))
help(fatorial)