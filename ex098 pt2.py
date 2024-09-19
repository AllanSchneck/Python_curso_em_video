from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)

    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ', flush=True)
            cont += p
            sleep(0.25)
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ', flush=True)
            cont -= p
            sleep(0.25)
        print('FIM')


contador(1,10,1)
contador(10,0,2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
pas = int(input('Digite o passo: '))
contador(ini, fim, pas)
