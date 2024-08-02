#2. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


user_time = str(input("Por favor, me diga qual turno você estuda? \n Para Matutino digite M \n Para Vespertino digite V \n Para Noturno digite N \n"))

if user_time == "M":
    print("Bom Dia!")
elif user_time == "V":
    print("Boa Tarde!")
elif user_time == "N":
    print("Boa Noite!")
else:
    print("Valor Invalido")