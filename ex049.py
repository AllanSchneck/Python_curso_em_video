n = int(input('DIGITE UM NÚMERO E VEJA SUA TABUADA: '))
print('\033[31m=-' * 11)
print('\033[32;40mA TABUDA DE {} \033[m'.format(n))
for c in range(0,10+1):
    print('\033[36;40m{}x{}={}\033[m'.format(c,n,c*n))
print('\033[31m=-' * 11)


