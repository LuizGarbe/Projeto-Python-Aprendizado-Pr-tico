import random

def play():
    primeira_parte()
    palavra_secreta = adivinha_palavras()
    letra_certa = letras_acertadas(palavra_secreta)

    print("Digite letras de (A) até (Z) para descobrir a palavra secreta.")
    print("O tema desse jogo é (frutas)")
    print(letra_certa)

    acertou = False
    enforcou = False
    errou = 0

    while (not acertou and not enforcou):
        chute = pede_chute()
        if chute in palavra_secreta:
            chute_correto(chute, letra_certa, palavra_secreta)
        else:
            errou += 1
            print("Você errou faltão {}".format(7 - errou))
            desenha_forca(errou)
        
        enforcou = errou == 7
        acertou = "_" not in letra_certa
        print(letra_certa)

    if acertou:
        imprime_mensagem_vencedor()
        print("A palavra era {}".format(palavra_secreta))
    else:
        imprime_mensagem_perdedor()
        
def primeira_parte():
     print("*********************")
     print("*Bem vindo a o jogo!*")
     print("*********************")

def adivinha_palavras():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linhas in arquivo:
        linhas = linhas.strip()
        palavras.append(linhas)
    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def letras_acertadas(palavra):
    return ["_" for letra in  palavra]

def pede_chute():
    chute = input("Qual a letra: ")
    chute = chute.strip().upper()
    return chute

def chute_correto(chute, letra_certa, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letra_certa[index] = letra
        index += 1
        
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       _____      ")
    print("      '.=====.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         .' '.        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor():
    print("Puxa, você foi enforcado!")
    print("    _____         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \_      XXX      _/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \___/           ")

def desenha_forca(erros):
    print("  ___     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("|__         ")
    print()

if(__name__ == "__main__"):
    play()