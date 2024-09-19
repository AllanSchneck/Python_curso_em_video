jogador = dict()
gol = list()
total = 0
jogador['nome'] = str.upper(input('Nome: ')).strip()
partidas = int(input('Quantas partidas jogadas: '))
for c in range(1, partidas+1):
    gol.append(int(input(f'Gols da {c}° partida: ')))
jogador['gols'] = gol
for g in gol:
    total += g
jogador['total'] = total
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k,v in jogador.items():
    print(f'{k} tem valor {v}')
print('-=' * 30)
print(f'O Jogador {jogador["nome"]} jogou {partidas} partidas')
for v,i in enumerate(gol):
    print(f'Na {v+1}° partida fez {i} gols')
print(f'Foi um total de {total} gols')
print('-=' * 30)
