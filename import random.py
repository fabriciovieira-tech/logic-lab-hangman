import random

def desenha_forca(erros):
    estagios = [
        "  +---+ \n  |   | \n      | \n      | \n      | \n      | \n=========",
        "  +---+ \n  |   | \n  O   | \n      | \n      | \n      | \n=========",
        "  +---+ \n  |   | \n  O   | \n  |   | \n      | \n      | \n=========",
        "  +---+ \n  |   | \n  O   | \n /|   | \n      | \n      | \n=========",
        "  +---+ \n  |   | \n  O   | \n /|\\  | \n      | \n      | \n=========",
        "  +---+ \n  |   | \n  O   | \n /|\\  | \n /    | \n      | \n=========",
        "  +---+ \n  |   | \n  O   | \n /|\\  | \n / \\  | \n      | \n========="
    ]
    print(estagios[erros])

def jogar_partida():
    palavras = ["python", "tecnologia", "hardware", "sistemas", "automacao", "interface"]
    palavra_secreta = random.choice(palavras).upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    
    fim_de_jogo = False
    venceu = False
    erros = 0
    letras_tentadas = []

    print("\n" + "="*20)
    print("NOVA PARTIDA INICIADA!")
    print("="*20)

    while not fim_de_jogo:
        print(f"\nPalavra: {' '.join(letras_acertadas)}")
        print(f"Erros: {erros}/6 | Tentativas: {letras_tentadas}")

        chute = input("Digite uma letra ou a palavra completa: ").strip().upper()

        if not chute or not chute.isalpha():
            print(">> ENTRADA INVÁLIDA! Use apenas letras.")
            continue

        if len(chute) > 1:
            if chute == palavra_secreta:
                letras_acertadas = list(palavra_secreta)
                venceu = True
                fim_de_jogo = True
            else:
                print(f"\nERRO FATAL! A palavra não era '{chute}'.")
                erros = 6
                fim_de_jogo = True
            continue

        if chute in letras_tentadas:
            print(f"Você já tentou a letra '{chute}'!")
            continue

        letras_tentadas.append(chute)

        if chute in palavra_secreta:
            for index, letra in enumerate(palavra_secreta):
                if chute == letra:
                    letras_acertadas[index] = letra
        else:
            erros += 1
            desenha_forca(erros)

        venceu = "_" not in letras_acertadas
        fim_de_jogo = venceu or erros == 6

    if venceu:
        print(f"\nPARABÉNS! Você descobriu a palavra: {palavra_secreta}")
    else:
        print(f"\nGAME OVER! Você foi enforcado. A palavra era: {palavra_secreta}")

def menu_principal():
    print("*" * 35)
    print("   BEM-VINDO AO JOGO DA FORCA   ")
    print("*" * 35)
    
    while True:
        jogar_partida()
        
        # Pergunta ao usuário se quer continuar
        resposta = input("\nDeseja jogar novamente? (S/N): ").strip().upper()
        
        if resposta != 'S':
            print("\nObrigado por jogar! Até a próxima.")
            break # Quebra o loop principal e encerra o programa

if __name__ == "__main__":
    menu_principal()
import random

def desenha_forca(erros):
    estagios = [
        "  +---+ \n  |   | \n      | \n      | \n      | \n      | \n=========",
        "  +---+ \n  |   | \n  O   | \n      | \n      | \n      | \n=========",
        "  +---+ \n  |   | \n  O   | \n  |   | \n      | \n      | \n=========",
        "  +---+ \n  |   | \n  O   | \n /|   | \n      | \n      | \n=========",
        "  +---+ \n  |   | \n  O   | \n /|\\  | \n      | \n      | \n=========",
        "  +---+ \n  |   | \n  O   | \n /|\\  | \n /    | \n      | \n=========",
        "  +---+ \n  |   | \n  O   | \n /|\\  | \n / \\  | \n      | \n========="
    ]
    print(estagios[erros])

def jogar_partida():
    palavras = ["python", "tecnologia", "hardware", "sistemas", "automacao", "interface"]
    palavra_secreta = random.choice(palavras).upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    
    fim_de_jogo = False
    venceu = False
    erros = 0
    letras_tentadas = []

    print("\n" + "="*20)
    print("NOVA PARTIDA INICIADA!")
    print("="*20)

    while not fim_de_jogo:
        print(f"\nPalavra: {' '.join(letras_acertadas)}")
        print(f"Erros: {erros}/6 | Tentativas: {letras_tentadas}")

        chute = input("Digite uma letra ou a palavra completa: ").strip().upper()

        if not chute or not chute.isalpha():
            print(">> ENTRADA INVÁLIDA! Use apenas letras.")
            continue

        if len(chute) > 1:
            if chute == palavra_secreta:
                letras_acertadas = list(palavra_secreta)
                venceu = True
                fim_de_jogo = True
            else:
                print(f"\nERRO FATAL! A palavra não era '{chute}'.")
                erros = 6
                fim_de_jogo = True
            continue

        if chute in letras_tentadas:
            print(f"Você já tentou a letra '{chute}'!")
            continue

        letras_tentadas.append(chute)

        if chute in palavra_secreta:
            for index, letra in enumerate(palavra_secreta):
                if chute == letra:
                    letras_acertadas[index] = letra
        else:
            erros += 1
            desenha_forca(erros)

        venceu = "_" not in letras_acertadas
        fim_de_jogo = venceu or erros == 6

    if venceu:
        print(f"\nPARABÉNS! Você descobriu a palavra: {palavra_secreta}")
    else:
        print(f"\nGAME OVER! Você foi enforcado. A palavra era: {palavra_secreta}")

def menu_principal():
    print("*" * 35)
    print("   BEM-VINDO AO JOGO DA FORCA   ")
    print("*" * 35)
    
    while True:
        jogar_partida()
        
        # Pergunta ao usuário se quer continuar
        resposta = input("\nDeseja jogar novamente? (S/N): ").strip().upper()
        
        if resposta != 'S':
            print("\nObrigado por jogar! Até a próxima.")
            break # Quebra o loop principal e encerra o programa

if __name__ == "__main__":
    menu_principal()

