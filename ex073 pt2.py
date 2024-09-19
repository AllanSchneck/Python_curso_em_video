times = ('Botafogo', 'Palmeiras', 'São Paulo', 'Atlético-MG', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Fluminense',
         'Fortaleza', 'Bragantina', 'Athletico-PR', 'Santos', 'Internacional', 'Corinthians', 'Cuiabá', 'Bahia',
         'Goiàs', 'Vasco da Gama', 'América-MG', 'Curitiba')
print('-=' * 13)
print(f'Lista de Time: {times}')
print('-=' * 13)
print(f'Os 5 primeiros são {times[0:5]}')
print(f'Os 4 últimos são {times[-4:]}')
print(f'Os times em ordem alfábetica é {sorted(times)}')
print(f'Internacional está na {times.index("Internacional")+1}° posição')