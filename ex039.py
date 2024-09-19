from datetime import datetime
a = int(input('Qual o ano do seu nascimento: '))
c = datetime.now()
d = (c.year - a)
if d == 18:
    print('\033[33mEstá na hora de se alistar você ja completou ou irá completar {} anos!'.format(d))
elif d < 18:
    print('\033[34mAinda não está na hora de você se alistar você possui apenas {} anos'.format(d))
    print('faltam {} anos para você se alistar!'.format(18-d))
else:
    print('\033[31mjá passou da hora de se alistar você tem {} anos procure se informar pois isso é grave!'.format(d))
    print('passou {} anos do prazo seu alistamento foi em {} você pode se alistar ainda em {}!'.format(d-18,a+18,c.year))
