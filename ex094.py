pessoa = dict()
pessoas = list()
mulheres = list()
velho = list()
media = 0
print('CADASTRE-SE JÁ!')
while True:
    pessoa['nome'] = str.title(input('Nome: ')).strip()
    pessoa['idade'] = int(input('Idade: '))
    sexo = str.upper(input('DIGITE SEU SEXO [M/F]: ')).strip()[0]
    while sexo not in 'FM':
        sexo = str.upper(input('DIGITE NOVAMENTE SEU SEXO [M/F]: ')).strip()[0]
    pessoa['sexo'] = sexo
    pessoas.append(pessoa.copy())
    pessoa.clear()
    resp = str.lower(input('Quer continuar?[S/N]: ')).strip()[0]
    while resp not in 'sn':
        resp = str.lower(input('Quer continuar [S/N]: ')).strip()[0]
    if 'n' in resp:
        break
print(f'Foram feitos o total de {len(pessoas)} cadastros')
for c in pessoas:
    for i in c.values():
        if i == c["idade"]:
            media += i
        if i == 'F':
            mulheres.append(c['nome'])
media = (media/len(pessoas))
print(f'Média idade do grupo é de {media:.2f} anos')
if len(mulheres) > 0:
    print(f'Todas as mulheres cadastradas foram {mulheres}')
else:
    print('Não foi cadastrada nenhuma mulher!')
for c in pessoas:
    for i in c.values():
        if i == c['idade']:
            if i >= media:
                velho.append(c['nome'])
print(f'Lista das pessoas acima da média idade é {velho}')
