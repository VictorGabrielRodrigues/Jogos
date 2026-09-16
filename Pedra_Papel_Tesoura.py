import random

print("\n#-----------------Iniciando o Jogo-----------------#")
print("\n#---------------Pedra  Papel  Tesoura---------------#\n")
opcao={
    "Pedra":1,
    "pedra":1,
    "Papel":2,
    "papel":2,
    "Tesoura":3,
    "tesoura":3
}
while True:
    opcao_humano=input("Escolha entre Pedra, Papel ou Tesoura: ")
    if opcao_humano in opcao:
        opcao_humano=opcao[opcao_humano]
        break
    else:
        print("Por favor, Escolha uma opção valida")

opcao_computadorl=random.choice(["Pedra","Papel","Tesoura"])
opcao_computador=opcao[opcao_computadorl]
    
if opcao_humano==opcao_computador:
    print("\n#---------------Ouve um Empate---------------#")
    print(f"\n#---------O Robo escolheu {opcao_computadorl} ---------#")
    
if ((opcao_humano==1 and opcao_computador==3) or 
      (opcao_humano==2 and opcao_computador==1) or 
      (opcao_humano==3 and opcao_computador==2)):
    
    print("\n#---------------Você Ganhou!!!---------------#")
    print(f"\n#---------O Robo escolheu {opcao_computadorl} ---------#")
    
else:
    print("\n#---------------Você Perdeu!---------------#")
    print(f"\n#---------O Robo escolheu {opcao_computadorl} ---------#")