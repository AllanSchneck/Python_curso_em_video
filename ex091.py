from random import randint
from time import sleep
jogadores = dict()
pos = 0
print('--- VALORES SORTEADOS ---')
sleep(1)
for c in range(1,5):
    dado = randint(1,6)
    jogadores[f'jogador{c}'] = dado
for k,v in jogadores.items():
    print(f'{k} jogou {v}')
    sleep(1)
print('--- O RANK ---')
sleep(1)
print('-=' * 15)
for rank in sorted(jogadores, key=jogadores.get, reverse=True):
    pos += 1
    print(f'{pos}° lugar: {rank} jogou {jogadores[rank]}')
    sleep(1)
print('-=' * 15)
