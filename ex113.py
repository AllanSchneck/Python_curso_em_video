def leiaInt(n='0'):
    while True:
        try:
            n = int(input('\033[33;1;40mDigite um número inteiro:\033[m '))
        except Exception as erro:
            print(f'\033[33;1mO Número digitado é Inválido pela exceção: \033[31m{erro.__class__}\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31;1mEntrada de dados bloqueda pelo usuário!\033[m')
            return 0
        else:
            return n


num = leiaInt()
print(f'\033[32mO número digitado foi {num}\033[m')


def leiaFloat(n=0):
    while True:
        try:
            n = float(input('\033[33;1;40mDigite um número real:\033[m '))
        except Exception as erro:
            print(f'\033[31;1mDigite um Número real válido! Exceção: {erro.__class__}\033[m')
        except KeyboardInterrupt:
            print('\033[31;1mEntrada de dados bloqueada pelo usuário!\033[m')
            return 0
        else:
            return n


numero = leiaFloat()
print(f'\033[32mO valor float digitado foi {numero:.2f}')
