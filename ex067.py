s = 1
print('-=' * 10)
print('TABUADA AUTOMÁTICA ESCOLHA UM NÚMERO E VEJA')
print('-=' * 10)
print('Quando quiser parar digite 0')
n = int(input('Digite um número: '))
while True:
    print(f'{n}X{s}={n * s}')
    s += 1
    if s == 11:
        print('Escolha outro número para ver sua tabuada.')
        n = int(input('Digite: '))
        s = 0
    if n <= 0:
        break
print('FIM')
