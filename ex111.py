from ex111UtilidadeCeV import moeda
p = float(input('Digite o preço: R$'))
moeda.resumo(p, 35, 22)
print(F'Aumentando 35%, temos {moeda.aumentar(p, 35)}')
print(F'Reduzindo 22%, temos {moeda.diminuir(p, 22)}')
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,True)}')
print(f'O dobro de {moeda.moeda(p)} ´e {moeda.dobro(p,True)}')
