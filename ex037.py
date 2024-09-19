n = int(input('Digite qualquer número inteiro: '))
q = str(input('Agora responda você quer converção em hexagonal, binária ou octal? '))
if ('Binária' == q) or ('binaria' == q) or ('bin' == q) or ('binario' == q) or ('Binário' == q):
    print('\033[1;32;40mSeu número em binários é {}\033[m'.format(bin(n)))
elif ('Hexagonal' == q) or ('hexagonal' == q) or ('hex' == q) or ('Hex' == q):
    print('\033[1;34;107mSeu número em hexagonal é {}\033[m'.format(hex(n)))
elif ('Octal' == q) or ('octal' == q) or ('oct' == q):
    print('\033[1;30;107mSeu número em octal é {}\033[m'.format(oct(n)))
else:
    print('\033[31mNão entendi repita o procedimento e leia com atenção!')
