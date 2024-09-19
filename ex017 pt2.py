c1 = float(input('Digite o comprimento do cateto oposto: '))
c2 = float(input('Digite o comprimento do cateto adjacente: '))
n = (c1 ** 2 + c2 ** 2) ** (1/2)
print('O comprimento da hipotenusa desse triângulo retângulo {:.2f}'.format(n))
