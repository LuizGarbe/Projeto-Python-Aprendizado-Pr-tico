import segundo
import inicial

def menu():
    print("*********************")
    print("**Escolha seu jogo!**")
    print("*********************")

    print("(1) jogo de adivinhar e (2) jogo de carro ")

    jogo = int(input("fala garai qual porra você quer: "))

    if (jogo == 1):
        print("Jogo de numero 1")
        inicial.jogar()
    elif (jogo == 2):
        print("jogo de adivinha fruta")
        segundo.play()

if(__name__ == "__main__"):
    menu()