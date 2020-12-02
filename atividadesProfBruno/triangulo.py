# Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. 


a, b, c = map(float, input("Indique três lados de um triângulo: ").split(" "))


def cond_exist(a, b, c):
    if(b - c  < a < b + c) and (a - c  < b < a + c) and (a - b  < c < a + b):
        print("É um triangulo")
        triangulo(a, b, c)
    else:
        print("Não é um triangulo")


def triangulo(a, b, c):
    if a == b == c:
        print("TRIÂNGULO EQUILÁTERO")
    elif a != b and a != c and b!=c:
        print("TRIÂNGULO ESCALENO")
    elif (a == b and a != c and b != c) or (b == c and b!= a and c!= a) or (a == c and a!= b and c!= b):
        print("TRIANGULO ISÓSCELES") 
    else:
        print("Outro tipo de triângulo")

cond_exist(a, b, c)
    

