from time import sleep


def contador(inicio, fim, passo):
    print('-' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo == 0:
        passo = 1
    if inicio <= fim and passo > 0:
        for c in range(inicio, fim + 1, passo):
            print(c, end=' ')
            sleep(0.25)
        print()
    elif fim < inicio and passo > 0:
        for c in range(inicio, fim-1,- passo):
            print(c, end=' ')
            sleep(0.25)
        print()
    else:
        if inicio <= fim:
            for c in range(fim, inicio-1, +passo):
                print(c, end=' ')
                sleep(0.25)
            print()
        if fim < inicio:
            for c in range(inicio, fim-1, passo):
                print(c, end=' ')
                sleep(0.25)
            print()
    print('-' * 30)


contador(1,10,1)
contador(10,0,2)
print('Contagem personalizada')
contador(int(input('Digite o inicio: ')),
         int(input('Digite o fim: ')),
         int(input('Digite de o passo: ')))
