"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
""Assassino"".
Caso contrário,ele será classificado como""Inocente"". 

"""
QuestionList = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']
AnswerList = []
v = "v"

for i in range(5):
    print(QuestionList[i])
    answer = input("Digite v para Verdadeiro \n Digite f para Falso: \n")
    AnswerList.append(answer)

if AnswerList.count(v) == 2:
    print("Você foi classificado como suspeito")

elif AnswerList.count(v) == 3 or AnswerList.count(v) == 4:
    print("Você foi classificado como Cumplice")

elif AnswerList.count(v) == 5:
    print("Você foi classificado como Assasino")
else:
    print("Você foi classificado como Inocente")
