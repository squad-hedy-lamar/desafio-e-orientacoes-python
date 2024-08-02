'''
Implemente um programa que classifique um aluno com base em sua pontuação em um exame. 
O programa deverá solicitar uma nota de 0 a 10. 
Se a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é reprovado.
'''

while True:
    nota = float(input('Digite sua pontuação no seu exame: '))
    if nota >= 7:
        print('Você foi aprovado!')
        break
    else:
        print('Você foi reprovado!')
        break