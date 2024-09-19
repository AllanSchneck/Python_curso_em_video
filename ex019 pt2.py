from random import choice
n1 = str(input('primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
n = [n1,n2,n3,n4]
s = choice(n)
print('O vencedor entre {},{},{} e {} É .... {} Parabéns!!!!'.format(n1,n2,n3,n4,s))
