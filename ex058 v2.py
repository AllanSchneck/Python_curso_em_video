from random import randint
c = randint(0, 10)
print('Sou seu computador acabei de pensar em um núemro entre 0 e 10 será que você consegue adivinhar')
print('Qual foi o número?')
p = 0
a = False
while not a:
    j = int(input('Qual seu palpite? '))
    p += 1
    if j == c:
        a = True
    if j != c:
        print('\033[31mTente novamente\033[m')
print('\033[32mAcertou\033[m')
print('Você fez {} palpites para acertar'.format(p))
