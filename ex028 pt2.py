from random import randint
from time import sleep
c = randint(0,5)
print('-=-'*10)
print('Vou pensar em um número de 0 a 5 tente adivinhar!!!')
sleep(4)
j = int(input('Em que número eu pensei? '))
if j==c:
    print('Parabéns você acertou pensei extamento no número {}'.format(c))
else:
    print('Você errou pensei no número {}'.format(c))