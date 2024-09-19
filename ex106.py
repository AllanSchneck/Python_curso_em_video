def manual():
    from time import sleep
    while True:
        print("\033[30;1;42m~" * 30)
        print('    SISTEMA DE AJUDA PyHELP')
        print('~' * 30)
        fun = str(input('\033[mFunção ou Biblioteca -> '))
        print('\033[34;1;107m-' * 40)
        print(f"   ACESSANDO O MANUAL DO COMANDO {fun}")
        print('-' * 40)
        sleep(1.5)
        print('\033[30;1;107m')
        help(fun)
        print('\033-' * 30)
        resp = str.upper(input('\033[mQuer continuar?[S/N]: ')).strip()[0]
        print('-' * 30)
        if resp not in 'SN':
            print('\033[mDigite apenas sim ou não')
            resp = str.upper(input('Quer continuar?[S/N]: ')).strip()[0]
        if resp in 'N':
            print('\033[31;1;40mFIM\033[m')
            break


manual()
