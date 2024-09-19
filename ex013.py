S = float(input('Digite O sálario do funcionário: '))
A = (S+(S/100*15))
N = input('Digite o nome do seu funcionário: ')
print('Parabéns \033[31m{}\033[m você recebeu uma promoção de \033[33m15%\033[m passando seu sálario de '
      '\033[32mR${}\033[m para \033[32mR${:.2f}\033[m'.format(N, S, A))
