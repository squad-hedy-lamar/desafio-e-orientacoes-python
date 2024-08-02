'''
Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda.
'''


salario_bruto = float(input('Digite seu salário bruto, separando os centavos por ponto: '))

if salario_bruto <= 1903.98:
    desconto_ir = 0
    salario_liquido = salario_bruto - desconto_ir
    print(f'Seu salário líquido é: {salario_liquido:.2f}')
elif salario_bruto > 1903.98 and salario_bruto <= 2826.65:
    desconto_ir = salario_bruto * 0.075
    salario_liquido = salario_bruto - desconto_ir
    print(f'Seu salário líquido é: {salario_liquido:.2f}')
elif salario_bruto > 2826.65 and salario_bruto <= 3751.05:
    desconto_ir = salario_bruto * 0.15
    salario_liquido = salario_bruto - desconto_ir
    print(f'Seu salário líquido é: {salario_liquido:.2f}')
elif salario_bruto > 3751.05 and salario_bruto <= 4664.68:
    desconto_ir = salario_bruto * 0.225
    salario_liquido = salario_bruto - desconto_ir
    print(f'Seu salário líquido é: {salario_liquido:.2f}')  
else:
    desconto_ir = salario_bruto * 0.275
    salario_liquido = salario_bruto - desconto_ir
    print(f'Seu salário líquido é: {salario_liquido:.2f}')