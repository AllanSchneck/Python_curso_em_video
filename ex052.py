n = int(input("Verificar numeros primos até: "))
mult = 0
for i in range(2,n):
    if (n % i == 0):
        mult += 1
if(mult==0):
    print("\033[32mÉ primo")
else:
    print("\033[31mNÃO É PRIMO")
