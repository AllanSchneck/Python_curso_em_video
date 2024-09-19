cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
        'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'dezessete', 'dezoito', 'dezanove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 a 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'você digitou o número {cont[num]}')
