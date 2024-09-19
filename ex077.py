t = ('Dinheiro', 'Salario', 'Trabalho', 'Programaçao', 'Python', 'Harmonia', 'Jogos', 'mente', 'pular', 'arcade',
     'Demanda', 'Banco', 'investimento')
for c in t:
     print(f'\nNa palavra {c.upper()} temos ', end='')
     for letra in c:
          if letra.lower() in 'aeiou':
               print(letra, end=' ')
