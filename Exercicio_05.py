'''
5. Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas

'''


lados = []
for i in range(3):
    comprimento = float(input(f"Digite o comprimento do lado {i + 1}: "))
    lados.append(comprimento)

if lados[0] == lados[1] == lados[2]:
  print("Equilátero")
elif lados[0] == lados[1] or lados[1] == lados[2] or lados[0] == lados[2]:
  print("Isósceles")
else:
  print("Escaleno")
