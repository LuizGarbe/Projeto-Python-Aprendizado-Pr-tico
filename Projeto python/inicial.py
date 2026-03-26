import random

def jogar():
    print("*********************")
    print("*Bem vindo a o jogo!*")
    print("*********************")


    numero_secreto = random.randrange (1, 101) # gera numeros entre 1 e 100 
    numero_tentativas = 0
    pontos = 1000

    print("Qual o nivel de dificudade?")
    print("(1) Facil, (2) Médio, (3) Dificil")

    nivel = int(input("Defina o numero que deseja:"))


    if(nivel == 1):
        numero_tentativas = 20
    elif(nivel == 2):
        numero_tentativas = 15
    else:
        numero_tentativas = 10

    for chances in range(1, numero_tentativas + 1):
        print("você tem {} de {}".format(chances, numero_tentativas))
        chute_str = input("Digite um valor de 1 até 100: ")
        print("Vovê digitou", chute_str)
        chute = int(chute_str)

        acertou = chute == numero_secreto
        baixo = chute < numero_secreto
        alto = chute > numero_secreto

        if(chute < 1 or  chute > 100):
            print("******************************")
            print("*Digite um valor de 1 até 100*")
            print("******************************")

        if(acertou):
            print("*******************************")
            print("*Você acertou e fez {} pontos!*".format(pontos))
            print("*******************************")
            break
        else:
            if(baixo):
                print("*****************************************************")
                print("*Você erro! Mas o numero que chutou foi muito baixo.*")
                print("*****************************************************")
            elif(alto):
                print("***********************************************")
                print("*Você errou! Mas o numero que chutou foi alto.*")
                print("***********************************************")
            perdeu_pontos = abs(numero_secreto - chute)
            pontos = pontos - perdeu_pontos

    print("*************")
    print("*Fim de jogo*")
    print("*************")

if(__name__ == "__main__"):
    jogar()