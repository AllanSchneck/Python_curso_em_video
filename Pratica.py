try:
    a = int(input('Númerador: '))
    b = int(input('Denominador: '))
    f = a/b
except Exception as erro:
    print(f'\033[34mO erro do momento é \033[31m({erro.__cause__} e {erro.__class__})')
else:
    print(f'\033[32mO resultado é {f:.2f}')
finally:
    print('\033[35mVolte sempre muito Obrigado!')
ValueError