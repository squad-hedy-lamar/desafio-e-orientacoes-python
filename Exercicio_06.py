'''
6. Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:

avião = 600 km/h
carro = 100 km/h
ônibus = 80 km/h

'''

distancia = float(input("Digite a distância da viagem (em km): "))

velocidadeAviao = 600
velocidadeCarro = 100
velocidadeOnibus = 80

tempoAviao = distancia / velocidadeAviao
tempoCarro = distancia / velocidadeCarro
tempoOnibus = distancia / velocidadeOnibus

print(f"Tempo de viagem de avião: {tempoAviao:.2f} horas")
print(f"Tempo de viagem de carro: {tempoCarro:.2f} horas")
print(f"Tempo de viagem de ônibus: {tempoOnibus:.2f} horas")
