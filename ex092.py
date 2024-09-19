pessoa = dict()
pessoa['Nome'] = str.upper(input('Nome: ')).strip()
pessoa['Nascimento'] = int(input('Ano de Nascimento: '))
pessoa['Ctps'] = int(input('CTPS: '))
if pessoa['Ctps'] == 0:
    print('\033[31mNão possui Carteira de Trabalho!\033[m')
else:
    pessoa['Contrato'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Seu salário: '))
    pessoa['aposento'] = ((pessoa['Contrato']-pessoa['Nascimento'])+35)
    print(f'Você ira se aposentar com {pessoa["aposento"]} anos de idade')
for k,v in pessoa.items():
    print(f'{k} tem o valor {v}')
