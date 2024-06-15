import random

def escolher_palavra(palavras):
    return random.choice(palavras)

def display_forca(tentativas_restantes):
    forca_estados = [
        """
        +---+
        |   |
        |   |
        |   |
        |   |
        ======
        """,
        """
        +---+
        |   |
        |   O
        |   |
        |   |
        ======
        """,
        """
        +---+
        |   |
        |   O
        |   |
        |   |
        ======
        """,
        """
        +---+
        |   |
        |   O
        |   |
        |   |
        ======
        """,
        """
        +---+
        |   |
        |   O
        |   |
        |   |
        ======
        """,
        """
        +---+
        |   |
        |   O
        |   \
        |   |
        ======
        """,
        """
        +---+
        |   |
        |   O
        |  /|\
        |   |
        ======
        """,
        """
        +---+
        |   |
        |   O
        |  /|\
        |  /
        ======
        """
    ]
    print(forca_estados[tentativas_restantes])

def jogar():
    palavras = ["programacao", "desenvolvimento", "logica", "python", "algoritmo", "estrutura", "funcao", "classe", "objeto", "codigo"]
    palavra_secreta = escolher_palavra(palavras)
    palavra_oculta = ["_" for _ in palavra_secreta]
    tentativas_restantes = 6

    print("Bem-vindo ao Jogo da Forca!")
    print(f"Você tem {tentativas_restantes} tentativas restantes.")
    display_forca(tentativas_restantes)

    while True:
        chute = input("Digite uma letra: ").lower()

        if chute in palavra_oculta:
            print("Essa letra já foi adivinhada.")
        elif not chute.isalpha():
            print("Digite apenas letras.")
        else:
            acertou = False
            for i, letra in enumerate(palavra_secreta):
                if letra == chute:
                    palavra_oculta[i] = letra
                    acertou = True

            if acertou:
                print(f"Você acertou a letra {chute}!")
                print("".join(palavra_oculta))

            else:
                tentativas_restantes -= 1
                print("Você errou!")
                display_forca(tentativas_restantes)

            if tentativas_restantes == 0:
                print(f"Você perdeu! A palavra era: {palavra_secreta}")
                break

            if "_" not in palavra_oculta:
                print(f"Você ganhou! A palavra era: {palavra_secreta}")
                break

    print("Obrigado por jogar!")

if __name__ == "__main__":
    jogar()
