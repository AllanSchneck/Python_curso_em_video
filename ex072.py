numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'dezessete', 'dezoito', 'dezanove', 'vinte')
while True:
    n = int(input('Digite um número de 0 a 20 e veja por extenso: '))
    if n in range(0,21):
        print('\033[34m{}\033[m por extenso é \033[34m{}\033[m'.format(n, numeros[n]))
    else:
        print('\033[31mDIGITE APENAS NÚMEROS DE 0 ATÉ 20.\033[m')
    r = str.upper(input('Você quer continuar [S/N]? '))[0].strip()
    if 'N' in r:
        break
print('Fim')
