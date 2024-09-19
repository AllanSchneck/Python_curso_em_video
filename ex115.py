from time import sleep
pessoas = {'Allan': 18, 'Paula': 22, 'Carine': 27, 'Ana': 17, "Samanta": 33, 'Kleber': 22,
           'João': 12, 'Helena': 4}


def lista_de_pessoas(pessoa):
    while True:
        print('-' * 40)
        print('MENU PRINCIPAL'.center(40))
        print('_' * 40)
        print('\033[33m1\033[m - \033[34mVer pessoas Cadastradas\033[m')
        print('\033[33m2\033[m - \033[34mCadastrar Nova pessoa\033[m')
        print('\033[33m3\033[m - \033[34mSair\033[m')
        print('_' * 40)
        try:
            r = int(input('\033[33;1mSua opção: \033[m'))
        except Exception:
            print('\033[31;1mDigite um opção válida! Por favor!\033[m')
        except KeyboardInterrupt:
            print('\033[31;1mO usuário preferiu não informar os dados!\033[m')
        else:
            if r == 1:
                print('-' * 40)
                print('Lista de pessoas'.center(40))
                for k, v in pessoa.items():
                    print(f'{k}       \t{v} anos')
            elif r == 2:
                while True:
                    try:
                        while True:
                            a = str(input('Nome: '))
                            if a in pessoa:
                                print('\033[36;1mEsse Nome já existe !\033[m')
                            else:
                                pessoa.get(a)
                                break
                    except Exception:
                        print('\033[36;1mDigite um Nome válido!\033[m')
                    except KeyboardInterrupt:
                        print('\033[31;1mO usuário preferiu não informar os dados!\033[m')
                    else:
                        break
                while True:
                    try:
                        pessoa[a] = int(input('idade: '))
                    except Exception:
                        print('\033[36;1mDigite uma idade válida!\033[m')
                    except KeyboardInterrupt:
                        print('\033[31;1mO usuário preferiu não informar os dados!\033[m')
                    else:
                        break

            elif r == 3:
                print('\033[36;1;40mSaindo\033[m')
                sleep(1)
                print('\033[32;1;40m...\033[m')
                sleep(1)
                break
            else:
                print('\033[31;1mDigite um opção válida! Por favor!\033[m')


lista_de_pessoas(pessoas)
