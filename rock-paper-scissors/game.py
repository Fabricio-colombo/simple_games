import random

mao_pedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

mao_papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

mao_tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

player = int(input('Digite 1 para PEDRA, 2 para PAPEL e 3 para TESOURA: '))

if player not in [1, 2, 3]:
    print("Escolha inválida. Por favor, escolha 1, 2 ou 3.")
else:
    computer = random.randint(1, 3)

    print('JOGADA DO PLAYER')
    if player == 1:
        print(mao_pedra)
    elif player == 2:
        print(mao_papel)
    elif player == 3:
        print(mao_tesoura)

    print('\nJOGADA DA MÁQUINA')
    if computer == 1:
        print(mao_pedra)
    elif computer == 2:
        print(mao_papel)
    elif computer == 3:
        print(mao_tesoura)

    print('\n')

    if player == computer:
        print('EMPATOU!')
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        print('PLAYER WINS')
    else:
        print('PLAYER LOSES')
