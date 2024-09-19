from random import shuffle
n1 = str(input('primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceito nome: '))
n4 = str(input('Quarto nome: '))
n = [n1, n2, n3, n4]
shuffle(n)
print('A lsita de apresentações será {}'.format(n))
