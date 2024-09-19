a = float(input('Cite o comprimento de uma reta: '))
b = float(input('Digite outra comprimento de reta: '))
c = float(input('Agora última reta para possíbilidade da formação de um triângulo: '))
if a < b + c and b < a + c and c < a + b:
    print('\033[32mÉ possível fazer um triângulo com essas retas! ')
    if a == b == c:
        print('\033[35mEquilatero Todos os lados iguais!')
    elif a != b != c != a:
        print('\033[33mESCALENO Todos os lados diferentes!')
    else:
        print('\033[34mIsósceles dois lados iguais!')
else:
    print('\033[31mímpossivel fazer um triângulo!')
