jogadores = list()
jogador = dict()
total = 0
gols = list()
print('<<<TABELA DE ESTATISTICAS FUTEBOL>>>')
while True:
    jogador['nome'] = str.title(input('Nome do jogador: '))
    partidas = int(input('Quantas partidas jogadas: '))
    for c in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols na {c}° partida: ')))
    for g in gols:
        total += g
    jogador['gols'] = gols[:]
    jogador['total'] = total
    gols.clear()
    jogadores.append(jogador.copy())
    jogador.clear()
    resp = str.upper(input('Quer continuar [S/N]? ')).strip()[0]
    while resp not in 'NS':
        resp = str.upper(input('Quer continuar [S/N]? ')).strip()[0]
    if 'N' in resp:
        break
print('-=' * 15)
print('COD    NOME        GOLS    TOTAL')
for s,j in enumerate(jogadores):
    print(f'{s}',end='')
    for k,v in j.items():
        print(f'     {v}', end='')
    print()
print()
print('-=' * 15)
print('Use os CODIGOS para achar os jogadores')
while True:
    p = 0
    dado = int(input('\nMostrar dados de qual jogador?[999 para parar] '))
    for s,j in enumerate(jogadores):
        if s == dado:
            print(f'LEVANTAMENTO DO JOGADOR {j["nome"]}')
            for g in j['gols']:
                p += 1
                print(f'No jogo {p} fez {g} gols')
    print('-=' * 15)
    if dado == 999:
        break
