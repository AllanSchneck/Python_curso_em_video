aluno = dict()
aluno['NOME'] = str.upper(input('Nome: ')).strip()
aluno['MÉDIA'] = float(input(f'Média de {aluno["NOME"]}: '))
if aluno['MÉDIA'] >= 6:
    aluno['APROVEITAMENTO'] = 'Aprovado'
elif aluno['MÉDIA'] >= 5:
    aluno['APROVEITAMENTO'] = 'Recuperação'
else:
    aluno['APROVEITAMENTO'] = 'Reprovado'
print('-=' * 15)
for k,v in aluno.items():
    print(f'{k}: {v}')
print('-=' * 15)