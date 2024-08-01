'''
6. Vamos construir um jogo de forca. O programa escolherá aleatoriamente uma palavra secreta de uma lista predefinida. A palavra secreta será representada por espaços em branco, um para cada letra da palavra. O jogador terá um número limitado de 6 tentativas. Em cada tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente na palavra secreta, ela será revelada nas posições correspondentes. Se a letra não estiver na palavra, uma mensagem de erro deverá ser informada. Após um número máximo de erros, o jogador perde. O jogo continua até que o jogador adivinhe a palavra ou exceda o número máximo de tentativas.

'''

import random

def escolher_palavra():
    palavras = ["python", "programacao", "desenvolvimento", "computador", "algoritmo"]
    return random.choice(palavras)

def exibir_palavra_oculta(palavra, letras_corretas):
    return ' '.join([letra if letra in letras_corretas else '_' for letra in palavra])

def jogo_forca():
    palavra_secreta = escolher_palavra()
    letras_corretas = set()
    letras_erradas = set()
    tentativas_restantes = 6

    print("Bem-vindo ao jogo da forca!")
    print(f"A palavra tem {len(palavra_secreta)} letras.")

    while tentativas_restantes > 0:
        print("\nPalavra: ", exibir_palavra_oculta(palavra_secreta, letras_corretas))
        print("Letras erradas: ", ' '.join(letras_erradas))
        print(f"Tentativas restantes: {tentativas_restantes}")

        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra.")
            continue

        if letra in palavra_secreta:
            letras_corretas.add(letra)
            if all(letra in letras_corretas for letra in palavra_secreta):
                print(f"Parabéns! Você adivinhou a palavra: {palavra_secreta}")
                break
        else:
            letras_erradas.add(letra)
            tentativas_restantes -= 1
            if tentativas_restantes == 0:
                print(f"Você perdeu! A palavra era: {palavra_secreta}")

jogo_forca()
