#Jogo de Advinhação
import random

def jogar():

    n_secreto = random.randrange(1,101)
    numero_secreto = int(n_secreto)
    rodada = 1
    pontos = 1000

    print("*************************************")
    print("Bem Vindo ao Jogo de Adiviação !")
    print("*************************************")

    print('Qual o nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Defina o nível: '))
    print("*************************************")

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    while (rodada <= total_tentativas):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute_str = input("Digite um número entre 1 até 100: ")
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você Acertou !")
            break
        else:
            if (maior):
                print("Você Errou! O número informado e maior que o número secreto.")
            else:
                print("Você Errou! O número informado e menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1
    print('Pontos obtidos: {}'.format(pontos))
    print("Fim de Jogo")

if(__name__ == '__main__'):
    jogar()
