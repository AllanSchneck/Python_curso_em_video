from ex107 import moeda
num = float(input('Digite o preço: R$'))
print(f'O dobro de {num} é {moeda.dobro(num)}')
print(f'A metade de {num} é {moeda.metade(num)}')
print(f'Aumentando 10% de {num} é {moeda.aumentar(num, 10)}')
print(f'O diminuido 13% de {num} é {moeda.diminuir(num, 13)}')
