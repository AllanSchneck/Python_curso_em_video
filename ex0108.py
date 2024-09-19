from ex108 import moeda
num = float(input('Digite o preço: R$'))
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))} ')
print(f'Diminuido 50% de {moeda.moeda(num)} é {moeda.moeda(moeda.diminuir(num,50))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(num,10))}')
