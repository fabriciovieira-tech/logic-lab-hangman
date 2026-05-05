import random

def desenha_forca(erros):
    estagios = [
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n      | \n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
    ]
    print(estagios[erros])

def jogar_partida():
    palavra = random.choice(["python", "hardware", "sistemas", "automacao"]).upper()
    acertos = ["_" for _ in palavra]
    erros, tentadas = 0, []

    print(f"\n{'='*20}\nNOVA PARTIDA!\n{'='*20}")

    while erros < 6 and "_" in acertos:
        print(f"\nPalavra: {' '.join(acertos)}\nErros: {erros}/6 | Tentadas: {tentadas}")
        chute = input("Letra ou palavra: ").strip().upper()

        if not chute.isalpha():
            print(">> Entrada inválida!")
            continue

        if len(chute) > 1:
            if chute == palavra: acertos = list(palavra)
            else: erros = 6; print(f"Erro fatal! Era: {palavra}")
            break

        if chute in tentadas:
            print("Já tentou essa!")
            continue

        tentadas.append(chute)
        if chute in palavra:
            for i, l in enumerate(palavra):
                if chute == l: acertos[i] = l
        else:
            erros += 1
            desenha_forca(erros)

    venceu = "_" not in acertos
    print(f"\n{'PARABÉNS!' if venceu else 'GAME OVER!'} A palavra era: {palavra}")

def main():
    while True:
        jogar_partida()
        if input("\nJogar novamente? (S/N): ").strip().upper() != 'S':
            print("Até logo!"); break

if __name__ == "__main__":
    main()


