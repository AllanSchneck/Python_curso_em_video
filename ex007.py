n1 = float(input('Digite a nota do aluno: '))
n2 = float(input('Digite a segundanota do aluno'))
m = ((n1+n2)/2)
print('\033[4;33;40mSendo as notas do aluno do aluno {} e {} sua média ficará {}\033[m'.format(n1, n2, m))
