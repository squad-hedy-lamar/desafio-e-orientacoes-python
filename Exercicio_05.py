'''
Crie uma função chamada contar_vogais que recebe uma string como parâmetro. 
Implemente a lógica para contar o número de vogais na string e retorne o total de vogais. 
Solicite ao usuário para inserir uma frase e utilize a função para contar as vogais.
'''

def contar_vogais(frase):
    vogais = 'aeiouAEIOUãáéíóôãâúà'
    contador = 0
    for letra in frase:
        if letra in vogais:
            contador += 1
    return contador

frase = input('Digite uma frase: ')
total_vogais = contar_vogais(frase)
print(f'Número de vogais na frase: {total_vogais}')