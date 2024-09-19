boletim = list()
notas = []
medias = []
v = 0
a = 0
while True:
    aluno = str.upper(input('Nome: '))
    notas.append(aluno)
    nota = float(input('1° nota: '))
    notas.append(nota)
    nota = float(input('2° nota: '))
    notas.append(nota)
    medias.append((notas[1] + notas[2])/2)
    boletim.append(notas[:])
    notas.clear()
    r = str.lower(input('Quer continuar [S/N]? ')).split()[0]
    if 'n' in r:
        break
print('-=' * 15)
print('No. NOME       MÉDIA')
print('-=' * 15)
for c in medias:
    print(f'{v}  {boletim[v][0]}          {c}')
    v += 1
print('-=' * 15)
while True:
    a = int(input('Qual boletim você que ver?(DIGITE 999 PARA PARAR): '))
    if a == 999:
        print('............FINALIZANDO')
        break
    else:
        print(f'As notas de {boletim[a][0]} são:{boletim[a][1:]}')
print('<' * 10, 'VOLTE SEMPRE!', '>' * 10)
