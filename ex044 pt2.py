p = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão''')
o =int(input('QUAL A OPÇÃO DE PAGAMENTO? '))
if o == 1:
    print('á vista no dinheiro ou cheque tem 10% de desconto e ficará o valor de \033[32mR${:.2f}'.format(p-(p/100*10)))
elif o == 2:
    print('Á vista no cartão tem 5% de desconto ficando \033[32mR${:.2f}'.format(p-(p/100*5)))
elif o == 3:
    print('até 2x no cartão ficará em \033[32mR${:.2f}'.format(p))
elif o == 4:
    k = int(input('Em quantas vezes você deseja fazer? '))
    print('O valor ficará com 20 % de juros ficando \033[32mR${:.2f}'.format(p+(p/100*20)))
else:
    print('\033[31mOpção inválida de pagamento tente novamente!!')