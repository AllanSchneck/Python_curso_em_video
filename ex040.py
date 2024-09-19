n = float(input('Nota do aluno da primeira prova: '))
n1 = float(input('Nota do aluno na segunda prova: '))
m = ((n+n1)/2)
if m >= 7:
    print('\033[1;32mParabéns você está aprovado com média {:.1f}'.format(m))
elif m >= 5.0:
    print('\033[1;33mOpa sua média de {:.1f} está em risco deverá fazer RECUPERAÇÃO'.format(m))
else:
    print('\033[31mInfelizmente você não atingiu média e está REPROVADO com a nota de {:.1f}'.format(m))
