from datetime import datetime


def voto(a=0):
    """
    -> FUNÇÃO DE CONDIÇÂO PARA VOTAR DE ACORDO COM A IDADE

    :prompt a:  Recebe a idade do usuário
    :return:    Sem retorno

    """
    if a < 16:
        print(f'\033[31mCom {a} anos Não VOTA\033[m')
    elif 16 <= a < 18 or a > 70:
        print(f'\033[33mCom {a} anos VOTO é OPCIONAL\033[m')
    else:
        print(f'\033[32mCom {a} anos o VOTO é OBRIGATÓRIO\033[m')
    print('-' * 20)


print('-' * 20)
ano = int(input('Ano de nascimento: '))
nasc = datetime.now().year - ano
voto(nasc)
