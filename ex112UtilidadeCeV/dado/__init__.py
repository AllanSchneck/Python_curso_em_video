def leiaDinheiro(din):
    valido = False
    while valido is False:
        din = str(input('Digite o preço: R$')).strip()
        if din.strip() == '' or din.isalpha():
            print(f'\033[31mERRO ({din}) é um preço inválido\033[m')
        else:
            din = din.replace(',', '.')
            valido = True
            return float(din)
