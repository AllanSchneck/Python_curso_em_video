t = float(input('Digite o valor do produto: '))
print('O PRODUTO ESTÁ \033[1;32mR${}\033[m'.format(t))
print('Á VISTA NO DINHEIRO/CHEQUE ESTÁ COM 10% DE DESCONTO\nNO CARTÃO Á VISTA ESTÁ COM 5% DE DESCONTO')
print('EM ATÉ 2X NO CARTÃO PREÇO NORMAL\nEM ATÉ 3X OU MAIS 20% DE JUROS')
p = str(input('Qual metódo de pagamento você deseja fazer? para outra opção digite (mais): '))
c = p.lower()
w = t-(t/100*10)
r = t-(t/100*5)
q = 'dinheiro' in c or 'cheque' in c
s = 'cartão' in c or 'cartao' in c
g = '2' in c or 'duas' in c
f = '3' in c or 'mais' in c or ''
if True == q:
    print('o console terá valor de R${:.2f}'.format(w))
elif True == s:
    print('O valor do console será R${:.2f}'.format(r))
elif True == g:
    print('O valor do console será R${:.2f}'.format(t))
elif True == f:
    k = int(input('Em quantas vezes você vai querer fazer? '))
    print('O valor ficará em torno de {:.2f}'.format(t+(t/100*k)))
else:
    print('\033[31mOpção inválida de pagmento tente novamente!')