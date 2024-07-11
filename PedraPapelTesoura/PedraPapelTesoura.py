import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("""Escolha uma opcao
      0 = Pedra
      1 = Papel
      2 = Tesoura
""")
game_images = [rock, paper,scissors]

escolha = int(input("Sua escolha: "))
print("Sua escolha: ")
print(game_images[escolha])

escolha_computador = random.randint(0, 2)

print("Escolha da maquina: ")
print(game_images[escolha_computador])

if escolha == 0:
    if escolha_computador == 2:
        print("Voce ganhou!")
        
    elif escolha_computador == 1:
        print("Computador ganhou!")
        
    else:
        print("Parece que temos um empate.")
        
elif escolha == 1:
    if escolha_computador == 0:
        print("Voce ganhou!")
        
    elif escolha_computador == 1:
        print("Parece que temos um empate.")
        
    else:
        print("Computador ganhou!")
else:
    if escolha_computador == 0:
        print("Computador ganhou!")
        
    elif escolha_computador == 1:
        
        print("Voce ganhou!")
    else:
        print("Parece que temos um empate.")