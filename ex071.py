print('''BEM VINDO AO BANCO PYTHON
BANCO EXCLUSIVO QUE NÃO ACEITA MOEDAS! ''')
c = v = d = u = 0
n = int(input('Digite quantos reais você quer sacar: '))
while True:
    if n >= 50:
        n -= 50
        c += 1
    elif n >= 20:
        n -= 20
        v += 1
    elif n >= 10:
        n -= 10
        d += 1
    elif n < 10:
        n -= 1
        u += 1
    if n == 0:
        break
print(f'''{c} cédulas de R$50.00
{v} cédulas de R$20,00
{d} cédulas de R$10,00
{u} cédulas de R$1,00''')
