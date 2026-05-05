import random
def jogar():
    imprime_boas_vindas()

    palavras = ["python", "tecnologia", "hardware", "sistemas", "automacao", "interface"]
    palavra_secreta = random.choice(palavras).upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    
    fim_de_jogo = False
    venceu = False
    erros = 0
    letras_tentadas = []

    while not fim_de_jogo:
        print(f"\nPalavra: {' '.join(letras_acertadas)}")
        print(f"Erros: {erros}/6 | Letras tentadas: {letras_tentadas}")

        chute = input("Digite uma letra ou a palavra completa: ").strip().upper()

        # --- NOVA VALIDAÇÃO DE ENTRADA ---
        # Verifica se a entrada está vazia ou contém números/símbolos
        if not chute or not chute.isalpha():
            print(">> ENTRADA INVÁLIDA! Por favor, use apenas letras (A-Z).")
            continue 
        # ---------------------------------

        if len(chute) > 1:
            if chute == palavra_secreta:
                letras_acertadas = list(palavra_secreta)
                venceu = True
                fim_de_jogo = True
            else:
                print(f"\nERRO FATAL! Você tentou chutar a palavra '{chute}' e errou.")
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
        imprime_mensagem_vitoria()
    else:
        imprime_mensagem_derrota(palavra_secreta)

def imprime_boas_vindas():
    print("*" * 35)
    print("   BEM-VINDO AO JOGO DA FORCA   ")
    print("*" * 35)

def imprime_mensagem_vitoria():
    print("\nParabéns, você ganhou!")
    # ... (mesmo código visual anterior)

def imprime_mensagem_derrota(palavra_secreta):
    print(f"\nPuxa, você foi enforcado! A palavra era {palavra_secreta}")
    # ... (mesmo código visual anterior)

def desenha_forca(erros):
    # ... (mesmo código dos estágios anterior)
    pass 

if __name__ == "__main__":
    jogar()

