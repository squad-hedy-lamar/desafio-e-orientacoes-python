# 2 - Desafio: exercicio 10
# 10. Faça um programa que lê três números inteiros e os mostra em ordem crescente.

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))

numeros = [num1, num2, num3]
numeros_ordenados = sorted(numeros)
print("Os números em ordem crescente são:", numeros_ordenados)
