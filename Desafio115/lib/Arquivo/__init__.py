from Desafio115.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ouve um erro na criação do arquivo!')
    else:
        print(f'\033[32;1;40mArquivo {nome} criado com sucesso\033[m')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except Exception:
        print('\033[31;1mErro ao ler o arquivo!\033[m')
    except IndexError:
        print('\033[31;1mErro ao ler o arquivo!\033[m')
    else:
        cabeçalho('\033[30;1mPESSOAS CADASTRADAS\033[m')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>7} anos')


def cadastrar(arq, nome='<<Desconhecido>>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31;1Ouve um erro na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31;1mOuve um ERRO na hora de escrever os dados!\033[m')
        else:
            print(f'Novo registro de {nome} foi adicionado')
            a.close()
