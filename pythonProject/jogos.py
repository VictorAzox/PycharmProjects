import forca
import adivinha

def escolhe_jogo():
  print("####################")
  print("#Escolha o seu jogo#")
  print("####################")

  print("(1) Forca (2) Adivinhação")

  jogo = int(input("Qual o Jogo"))

  if (jogo == 1):
    print("Jogando Forca")
    forca.jogar()
  elif(jogo ==2 ):
    print("Jogando Adivinhação")
    adivinha.jogar()
if(__name__=="__main__"):
    escolhe_jogo()