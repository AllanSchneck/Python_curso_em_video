ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    media = ((nota1 + nota2)/2)
    ficha.append([nome, [nota1, nota2], media])
    resp = str.lower(input('Quer continuar?[S/N]: '))
    if 'n' in resp:
        break
print('-=' * 30)
print(f'{"No":<4}{"NOME":<10}{"MEDIA":>8}')
print('-=' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno?[999 interrompe]: '))
    if opc == 999:
        print('.........FINALIZANDO........')
        break
    if opc <= len(ficha) - 1:
        print(f'Nota de {ficha[opc][0]} são {ficha[opc][1:2]}')
print('<<< Volte sempre! >>>')
