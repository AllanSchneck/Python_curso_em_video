d = float(input('Qual a distância da sua viagem? '))
print('Você esta prestes a fazer uma viagem de {}KM'.format(d))
p = d*0.50 if d<=200 else d*0.45
print('O preço da sua passagem será e R${:.2f}'.format(p))