
def titulo(msg):
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))


titulo('          Área de Terrenos           ')
a = float(input('Digite a largura do Terreno (m): '))
b = float(input('Digite o comprimento do Terreno (m): '))


def area(a,b):
    calc = a*b
    print(f'A área do terreno de {a}x{b} é {calc:.2f}m2')


area(a,b)
