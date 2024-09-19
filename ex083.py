expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
print(pilha)
if len(pilha) == 0:
    print('\033[32mSua expressão está válida!')
else:
    print('\033[31mSua expressão está inválida!')
