# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

#     quantos espaços em branco existem na frase.
#     quantas vezes aparecem as vogais a, e, i, o, u.

frase = input("Escreva uma frase: ").upper()

cont_espacos = 0
vogais = []
    
def contador(frase, cont_espacos, vogais):
    for letra in frase:
        if (letra == " "):
            cont_espacos +=1
        elif(letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U'):
            vogais.append(letra)
            qtd_vogal = len(vogais)
            a = vogais.count('A')
            e = vogais.count('E')
            i = vogais.count('I')
            o = vogais.count('O')
            u = vogais.count('U')
    print(f"""\nContador de espaços e vogais:

        Na sua frase há:
        Espaços: {cont_espacos}
        Vogais A: {a}  E: {e}  I: {i}  O: {o}  U: {u}
    """)

contador(frase, cont_espacos, vogais)

#achei muito legal seu codigo todo parabéns :)