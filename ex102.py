
def fatorial(a=1, show=False):
    """
    -> CALCULO FATORIAL
     :prompt: a:      Recebe o número para ver seu fatorial
     :prompt: show:   recebe valor lógico para mostrar a operação ou não
     :return:         Sem retorno
    """
    f = 1
    for c in range(a, 0, -1):
        f *= c
        if show and c == a:
            print(f'{c}', end=' ')
        if show and c != 1 and c != a:
            print(f'x {c} ', end='')
    print(f'= {f}', end='')


print('FATORIAL DIGITE UM VALOR E VEJA O FATORIAL')
num = int(input('Digite um valor: '))
while True:
    sw = str.upper(input('Quer mostrar a operação [S/N]? ')).strip()[0]
    if sw in 'SN':
        break
if sw == 'S':
    sw = True
else:
    sw = False
fatorial(num, sw)
print(fatorial.__doc__)
