from ex109 import moeda
num = int(input('Digite um preço: R$'))
print(f'a metade de {moeda.moeda(num)} é {(moeda.metade(num, False))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(num, 10, True)}')
print(f'Diminuido 20%, temos {moeda.diminuir(num, 20, False)}')
