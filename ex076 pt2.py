t = ('Cigarro', 10.25, 'Pão', 5.20, 'Todynho', 2.50, 'Cerveja', 3.80, 'Salgadinho', 7.50, 'Danone', 3,'Água', 1.25,
     'Caneta', 1.50, 'Chiclete', 2,'Chocolate', 4.50, 'Refrigerante',8, 'Café', 20, 'Álcool', 11, 'Desodorante', 14.25)
print('-' * 30)
print('LISTAGEM DE PREÇOS')
print('-' * 30)
for c in range(0, len(t)):
    if c % 2 == 0:
        print(f'{t[c]:.<30}', end='')
    else:
        print(f'R${t[c]:>6.2f}')
