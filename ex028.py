import random
n = int(input('Que número estou pensando 0 a 5: '))
p = (0,1,2,3,4,5)
r = random.choice(p)
if n==(r):
    print('\033[32mParabéns você acertou o número era {}!!!!'.format(r))
else:
    print('\033[31mVocê errou tente novamente o número era {}'.format(r))
