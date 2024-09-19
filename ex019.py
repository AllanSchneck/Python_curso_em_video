import random
n = ('Allan', 'júlia', 'jussara', 'kleber')
n1 = (random.choice(n))
print('''O vencedor do sorteio entre \033[4;33m(Allan,júlia,jussara e kleber)\033[m é \033[32m{}\033[m Parabéns!!!
'''.format(n1))
