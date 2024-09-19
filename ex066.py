s = c = 0
print('-=' * 10)
print('\033[32;40;1mDigite números inteiros quando quiser parar digite 999.\033[m')
print('-=' * 10)
while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'\033[34mA soma dos números digitados é igual a {s}')
print(f'\033[34mForrm digitados {c} números.')
