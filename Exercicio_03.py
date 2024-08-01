#DESAFIO 1 - Exercicio 3 
#Faça um Programa que peça a quantidade de quilômetros, transformeem metros, centímetros e milímetros.
 
km_data = float(input("Por favor, digite a quandidade de quilômetros(KM)?"))

m_data = km_data * 1000
cm_data = km_data * 100000
mm_data = km_data * 1000000

print(f"O numero digitado foi, {int(km_data)} KM! Abaixo está a conversão para cada unidade de medida \n {int(km_data)} KM = {int(m_data)} M \n {int(km_data)} KM = {int(cm_data)} cm \n {int(km_data)} KM = {int(mm_data)} mm \n Obrigada!")
