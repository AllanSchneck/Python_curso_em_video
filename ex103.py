def ficha(nome, gols="0"):
    """
    -> Função de ficha para jogador de futebol

    :prompt nome:   RECEBERA O NOME DO JOGADOR
    :prompt gols:   RECEBERA QUANTIDADE DE GOLS QUE O JOGADOR MARCOU
    :return:        SEM RETORNO

    Parameters
    ----------
    nome
    gols

    Returns
    -------

    """
    if gols.isnumeric() == True:
        gols = int(g)
    else:
        gols = 0
    if nome.isalnum() == False:
        nome = '<<Desconhecido>>'
    print(f"O jogador {nome} marcou {gols} gol(s) no campeonato")


n = str(input("Nome do Jogador:"))
g = str(input('Digite quantos gols ele marcou: '))
ficha(n, g)
