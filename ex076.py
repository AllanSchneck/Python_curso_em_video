t = ('Cigarro', 'R$ 10.25', 'Pão', 'R$ 5.20', 'Todynho', 'R$ 2.50', 'Cerveja', 'R$ 3.80', 'Salgadinho', 'R$ 7.50',
     'Danone', 'R$ 3','Água', 'R$ 1.25', 'Caneta', 'R$ 1.50', 'Chiclete', 'R$ 2','Chocolate', 'R$ 4.50', 'Refrigerante',
     'R$ 8', 'Café', 'R$ 20', 'Álcool', 'R$ 11', 'Desodorante', 'R$ 14.25')
print('_' * 40)
print('           LISTAGENS DE PREÇO')
print('-' * 40)
s = 0
for c in t:
    s += 1
    if s == 2:
        print(c)
        s = 0
    elif s == 1:
        print(c, end='.' * 15)
print('_' * 40)
