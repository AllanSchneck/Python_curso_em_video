r = int(input('Qual velocidade o carro passou o radar? '))
m = ((r-80)*7)
if r <= 80:
    print('\033[32mTenha um bom dia e dirija com segurança\033[m')
else:
    print('\033[31mVocê ultrapssou o limite de velocidade terá que pagar uma multa de R${}\033[m'.format(m))