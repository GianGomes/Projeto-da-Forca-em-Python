import random

def mostrar_palavra(palavra, letras_certas):
    return ''.join([letra if letra in letras_certas else '_' for letra in palavra])

def forca():
    
    palavras = ["python","programação","desenvolvimento","tecnologia"]

    palavraSelecionada = random.choice(palavras)
    letras_certas = []
    letras_erradas = []
    tentativas_restantes = 6

    print("Vamos jogar forca?")
    print("Você precisa adivinhar a palavra antes das tentativas se esgotarem, então, pense bem!")

    while tentativas_restantes > 0:
        print("\nPalavra", mostrar_palavra(palavraSelecionada, letras_certas))
        print(f"Letras erradas {', '.join(letras_erradas)}")
        print(f"Tentativas restantes: {tentativas_restantes}")

        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("ATENÇÃO! Você pode digitar apenas uma letra.")
            continue

        if letra in letras_certas or letra in letras_erradas:
            print("Você já digitou essa letra, tente outra.")
            continue

        if letra in palavraSelecionada:
            print(f"VAMOO!! A letra '{letra}' está na palavra! Continue até acertar.")
            letras_certas.append(letra)

        else:
            print(f"Que pena. A letra '{letra}' não está na palavra. Você ainda tem '{tentativas_restantes}' chances.")
            letras_erradas.append(letra)
            tentativas_restantes -= 1

        if all(letra in letras_certas for letra in palavraSelecionada):
            print(f"\nVAMOO!! Você adivinhou a palavra: {palavraSelecionada}!")
            print(" ")
            print("Digite 'python trabForca.py' no seu terminal para jogar novamente.")
            break

        if tentativas_restantes == 0:
            print("\nQue pena, suas chances acabaram.")
            print(f"A palavra era: {palavraSelecionada}")
            print(" ")
            print("Digite 'python trabForca.py' no seu terminal para jogar novamente.")

if __name__ == "__main__":
    forca()