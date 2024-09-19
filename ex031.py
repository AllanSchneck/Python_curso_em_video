v = float(input('Quantos KM deu sua viagem? '))
m = (v*0.50)
m1 = (v*0.45)
if v<=200:
    print('\033[31mSua viagem de {}KM ficará em torno de R${}\033[m'.format(v,m))
else:
    print('\033[32mSua viagem de {}KM terá o custo de R${}\033[m'.format(v,m1))