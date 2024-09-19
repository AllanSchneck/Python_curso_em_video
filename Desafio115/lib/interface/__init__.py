
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except Exception:
            print('\033[31;1mDigite um número válido!\033[m')
        except KeyboardInterrupt:
            print('\033[31;1mO usuário preferiu não informar os dados\033[m')
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(43))
    print(linha())


def menu(lista):
    cabeçalho('\033[32;1;40mMENU PRINCIPAL\033[m')
    c = 1
    for item in lista:
        print(f'{c} -> {item}')
        c += 1
    print(linha())
    opc = leiaInt('\033[34;1;40mSua Opção:\033[m ')
    return opc
