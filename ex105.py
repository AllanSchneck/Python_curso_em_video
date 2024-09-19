
def notas(*num, sit=False):
    """
    -> Função de Notas para avaliar o aproveitamento de uma turma

    :prompt num:    Receberá as Notas dos alunos
    :prompt sit:    Mostrara a situação da turma [NÃO -> False] / [SIM -> True]
    :return:        Retornara um dicionário com as informações da turma


    Parameters
    ----------
    num
    sit

    Returns
    -------

    """
    turma = dict()
    turma["total"] = len(num)
    turma["Maior"] = max(num)
    turma["Menor"] = min(num)
    turma["Média"] = sum(num) / len(num)
    if sit:
        if turma["Média"] >= 7:
            turma["Situação"] = 'Muito Bom'
        elif turma["Média"] >= 6:
            turma["Situação"] = "Bom"
        elif turma["Média"] >= 5:
            turma["Situação"] = "Regular"
        else:
            turma["Situação"] = "Péssimo"
    return turma


alunos = notas(5.5, 2.5, 10, 6.5)
print(alunos)
