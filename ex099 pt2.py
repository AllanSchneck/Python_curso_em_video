

def maior(*num):
    print('-' * 20)
    print(f'Analisando valores {num}')
    print(f'O maior valor informado foi \033[31;1;40m{max(num)}\033[m')


maior(1, 8, 2, 7, 3, 5)
maior(2, 6, 4, 2, 1, 6, 8, 2348, 4)
maior(1, 2, 4, 5, 6, 9, 102, 423, 234239, 32423423423, 324289376452, 121)
