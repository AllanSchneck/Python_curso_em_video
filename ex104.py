def leaint(num):
    """
    -> FUNÇÃO INPUT PARA NÚMEROS

    :prompt num:  Receberá o número digitado
    :return:      O NÚMERO DIGITADO INTEIRO

    Parameters
    ----------
    num

    Returns
    -------

    """
    print('-' * 20)
    if num.isnumeric():
        num = int(num)
    else:
        print('\033[31;1;40mERRO! Digite apenas números inteiros!\033[m')
        while True:
            num = str(input('Digite um número: '))
            if num.isnumeric():
                num = int(num)
                break
            else:
                print('\033[31;1;40mERRO! Digite apenas números inteiros!\033[m')
    return num


n = leaint(input('Digite um número: '))
print(f'Você acabou de digitar {n}')
