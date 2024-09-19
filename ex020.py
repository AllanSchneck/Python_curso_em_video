import random
n = 'allan'
n2 = 'Kleber'
n1 = 'Julia'
n3 = 'Jussara'
lista = [n, n2, n1, n3]
random.shuffle(lista)
print('A ordem das apresentações de hoje sera \033[4;35m{}'.format(lista))
