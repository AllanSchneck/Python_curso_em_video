import random
n = range(0, 10)
q = random.choice(n)
c = 11
b = 0
while not q == c:
    c = int(input('\033[;40mTente adivinhar que valor estou pensando entre 0 a 10: \033[m'))
    if q != c:
        b += 1
        print('\033[31mErrou, Tente novamente\033[m')
print('\033[32mAcertou o número era {}\033[m'.format(q))
print('\033[34mVocê Tentou {} vezes para acertar'.format(b+1))
