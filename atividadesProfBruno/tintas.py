# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga 
# e sempre arredonde os valores para cima, isto é, considere latas cheias.

from time import sleep
m = float(input("Insira, em metros quadrados, a área a ser pintada: "))

m1 = m1 = m + (m * 0.1)
litro_nec = m1/6
valor_lata = 80
valor_galao = 25

def so_lata(litro_nec, valor_lata):
    lata = 18
    qtd_lata = litro_nec / lata
    red = round(qtd_lata + 0.5)
    print(f"Você irá precisar de {red} latas")
    print(f"Total de R$ {red*valor_lata:.2f}")
    

def so_galao(litro_nec, valor_galao):
    galao = 3.6
    qtd_galao = litro_nec / galao
    red = round(qtd_galao + 0.5)
    print(f"Você irá precisar de {red} galões")
    print(f"Total de R$ {red*valor_galao:.2f}")
    

def lata_galao(litro_nec, valor_galao, valor_lata):
    galao = 3.6
    lata = 18
    qtd_lata = litro_nec//lata
    resto = litro_nec%lata
    qdt_galao = resto/galao
    red = round(qdt_galao + 0.5)
    print(f"\nVocê irá precisar de {qtd_lata} latas + {red} galões")
    print(f"Total de R$ {red*valor_galao + qtd_lata*valor_lata:.2f}")
    

while True:

    opcao = int(input("""\n\t COMPRA DE TINTA

    1 - Ver litros necessários;
    2 - Ver custo comprando somente latas;
    3 - Ver custo comprando somente galões;
    4 - Ver custo comprando misto;
    5 - Sair.

    Valor Lata (18L) : R$ 80,00
    Valor Galão (3,6L) : R$ 25,00

    Digite a opção desejada: """))

    if opcao == 1:
        print(f"\n{litro_nec:.2f} Litros necessários")
        sleep(2)
    elif opcao == 2:
        so_lata(litro_nec, valor_lata)
        sleep(2)
    elif opcao == 3:
        so_galao(litro_nec, valor_galao)
        sleep(2)
    elif opcao == 4:
        lata_galao(litro_nec, valor_lata, valor_galao)
        sleep(2)
    elif opcao == 5:
        print("Obrigada pela preferência!")
        break










