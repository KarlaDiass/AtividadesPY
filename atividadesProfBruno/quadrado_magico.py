# Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, 
# com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. 
# Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

#     8  3  4 
#     1  5  9
#     6  7  2

# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. 
# Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. 
# Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3. 

from itertools import permutations
def quadrado_magico():
    print("\nPossíveis Quadrados Mágicos 3x3:\n")
    matriz = list(permutations([1,2,3,4,5,6,7,8,9]))

    for quadrado in matriz:
        
        if quadrado[4] == 5:
            soma_linha1 = quadrado[0] + quadrado[1] + quadrado[2]
            soma_linha2 = quadrado[3] + quadrado[4] + quadrado[5]
            soma_linha3 = quadrado[6] + quadrado[7] + quadrado[8]
            if soma_linha1 == soma_linha2 == soma_linha3:
                soma_coluna1 = quadrado[0] + quadrado[3] + quadrado[6]
                soma_coluna2 = quadrado[1] + quadrado[4] + quadrado[7]
                soma_coluna3 = quadrado[2] + quadrado[5] + quadrado[8]
                if soma_coluna1 == soma_coluna2 == soma_coluna3:
                    soma_diagonal1 = quadrado[0] + quadrado[4] + quadrado[8]
                    soma_diagonal2 = quadrado[2] + quadrado[4] + quadrado[6]
                    if soma_diagonal1 == soma_diagonal2:
                        print(end=" ")
                        
                        for i in range(0, 7, 3):
                            print(f"\t{quadrado[i]} {quadrado[i + 1]} {quadrado[i + 2]}\n", end=" ")
                        print('\n')
    
       
quadrado_magico()

            

     
