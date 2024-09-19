v = float(input('Qual o valor do imóvel? R$'))
s = float(input('Qual o salário que você recebe? '))
a = int(input('Em quantos anos você pretende pagar?'))
e = (s/100*30)
e1 = (s/100*35)
p = (v/(a*12))
if p <= e:
    print('\033[32mSeu emprestimo está aprovado, Parabéns pela sua nova casa!')
    print('\033[32mSerá cobrado R${:.2f} todo mês do seu saldo referente ao seu empréstimo'.format(p))
elif p <= e1:
    print('\033[34mBom podemos negociar a respeito do seu empréstimo.')
    print('\033[34mPodemos facilitar sua vida com a prorrogação dele ou seja em mais tempo.')
else:
    print('\033[31mSeu empréstimo foi recusado o valor do emprétimo será maior que 30% do seu salário!')
