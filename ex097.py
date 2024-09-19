def escreva(txt):
    print('~' * (len(txt)+2))
    print(f' {txt}')
    print('~' * (len(txt)+2))


escreva(str(input('Nome: ')))
escreva(str(input('Idade: ')))
escreva(str(input('Filme favorito: ')))