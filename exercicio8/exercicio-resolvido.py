# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.Calcule e mostre o total do seu salário no referido mês

valor_recebido_por_hora= float(input('Quanto você ganha por hora? '))
horas_trabalhadas_mes = int(input('Quantas horas você trabalhou no mês? '))
salario_total = valor_recebido_por_hora * horas_trabalhadas_mes

print(f'O Seu salário total no mês é: {salario_total:.2f}')