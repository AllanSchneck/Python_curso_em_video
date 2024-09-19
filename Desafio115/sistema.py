from Desafio115.lib.interface import *
from Desafio115.lib.Arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Lista de pessoas', 'Adicionar pessoas', 'sair'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('\033[35;1;40mNovo cadastro\033[m')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('\033[36;1msair\033[m')
        sleep(1)
        cabeçalho('\033[36;1;40mSaindo...\033[m')
        break
    else:
        print('\033[31;1mERRO...Digite uma opção válida\033[m')
    sleep(1)
