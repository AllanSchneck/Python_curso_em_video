n = int(input('Digite um valor qualquer: '))
n1 = int(input('Digite outro valor qualquer: '))
if n > n1:
    print('\033[1;34mO primeiro valor é maior {}'.format(n))
elif n1 > n:
    print('\033[1;30;107mO segundo valor é é maior {}\033[m'.format(n1))
else:
    print('\033[1;33;40mNão existe número maior os dois são iguais\033[m')