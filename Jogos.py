import Jogo_Forca
import Jogo_Adivinhacao

def escolhar_jogo():
    print('*****************************')
    print('****** Escolha o Jogo! ******')
    print('*****************************')

    print('(1) Forca , (2) Advinhação')
    jogo = int(input('Qual Jogo? '))

    if(jogo == 1):
        print('Jogo da Forca')
        Jogo_Forca.jogar()
    elif(jogo == 2):
        print('Adivicação')
        Jogo_Adivinhacao.jogar()

if(__name__ == '__main__'):
    escolhar_jogo()