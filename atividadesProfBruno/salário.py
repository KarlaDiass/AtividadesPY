# Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% 
# para o sindicato, faça um programa que nos dê:

#     salário bruto.
#     quanto pagou ao INSS.
#     quanto pagou ao sindicato.
#     o salário líquido.
#     calcule os descontos e o salário líquido, conforme a tabela abaixo: 
#     + Salário Bruto : R$
#     - IR (11%) : R$
#     - INSS (8%) : R$
#     - Sindicato ( 5%) : R$
#     = Salário Liquido : R$

def cal_salario(valor_horas, num_horas):
    sal_bruto = valor_horas * num_horas
    imp_renda = sal_bruto * 0.11 
    inss = sal_bruto * 0.08
    sind = sal_bruto * 0.05
    sal_liq = sal_bruto - (imp_renda + inss + sind)

    print(f"""\nDescontos e salário líquido, conforme a tabela abaixo: 
    
    - Salário Bruto : R$ {sal_bruto}
    - IR (11%) : R$ {imp_renda}
    - INSS (8%) : R$ {inss}
    - Sindicato ( 5%) : R$ {sind}
    - Salário Liquido : R$ {sal_liq} """)


try:
    valor_horas = float(input("\nInsira o valor que você ganha por hora: R$ "))
    num_horas = float(input("\nInsira o total do horas trabalhadas em um mês: "))
        
    cal_salario(valor_horas, num_horas)
except:
    print("ops")
    pass
