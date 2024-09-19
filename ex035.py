a = float(input('cite comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('agora comprimento da terceira reta: '))
t = b<a+c and a<b+c and c<a+b
if (t):
    print('\033[32mÉ possível fazer um triângulo com essas medidas')
else:
    print('\033[31mNão foi possível fazer um triângulo com essas medidas')