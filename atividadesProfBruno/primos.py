# Faça um programa que gera uma lista dos números primos existentes entre 1 e 
# um número inteiro informado pelo usuário. 



n = int(input("Verificar números primos de 1 até: "))

primos = []

for i in range(2,n):
    cont = 0
    for x in range(1, i+1):
        if i%x == 0:
            cont +=1
    if cont <=2:
        primos.append(i)

print("Os números primos de 1 até",n," são:" ,*primos, sep=' ')

# primeira vez que vejo esse sep achei massa.