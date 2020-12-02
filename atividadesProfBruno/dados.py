# Faça um programa que simule um lançamento de dados. 
# Lance o dado 100 vezes e armazene os resultados em um vetor. 
# Depois, mostre quantas vezes cada valor foi conseguido. 
# Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, 
# simulando os lançamentos dos dados. 

from random import randint
from time import sleep


valores_dado = []

for jogada in range(100):
    valores_dado.append(randint(1, 6))

um = valores_dado.count(1)
dois = valores_dado.count(2)
tres = valores_dado.count(3)
quatro = valores_dado.count(4)
cinco = valores_dado.count(5)
seis = valores_dado.count(6)

print("\nO dado foi lançado 100 vezes...")
sleep(2)
print(f"""
Quantidade de cada número sorteado:

|1 = {um} | 2 = {dois} | 3 = {tres} |
        
|4 = {quatro} | 5 = {cinco} | 6 = {seis} |
""")


