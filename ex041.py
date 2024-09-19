from datetime import datetime
d = int(input('Qual o ano do seu nascimento: '))
c = datetime.now()
a = (c.year - d)
if a > 20:
    print('Bom pela sua idade de {} anos você irà para categoria \033[1;33;107mMaster\033[m das competições'.format(a))
elif a >= 20:
    print('Na sua faixa etária de {} anos irá competir na categoria \033[1;31;40mSenior\033[m'.format(a))
elif a >= 19:
    print('Pela sua idade de {} sua categoria será \033[1;35;40mJunior\033[m'.format(a))
elif a >= 14:
    print('Como você tem apenas {} anos irá competir na cetegoria \033[1;36mInfantil\033[m'.format(a))
else:
    print('você é novo e tem {} anos participará das competições da categoria \033[4;32mMirim\033[m'.format(a))