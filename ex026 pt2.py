f = str(input('Digite uma frase: ')).lower().strip()
print('A letra a aparece {} vezes na frase'.format(f.count('a')))
print('A primeira vez que A aparece foi na posição {}'.format(f.find('a')+1))
print('A última letra A apareceu na posição {}'.format(f.rfind('a')+1))
