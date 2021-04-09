import random


def GameWin(you, comp):
    if you == comp:
        print("Game tie!")
    elif you == 0:
        if comp == 1:
            print("You loss the game!")
        if comp == 2:
            print("You win the game!")
    elif you == 1:
        if comp == 2:
            print("You loss the game!")
        if comp == 0:
            print("You win the game!")
    elif you == 2:
        if comp == 0:
            print("You loss the game!")
        if comp == 1:
            print("You win the game!")


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
while True:
    yourChoice = int(input("Enter 0 for rock, 1 for paper, 2 for scissors: "))
    print("Your Choice is:")
    if yourChoice == 0:
        print(rock)
    if yourChoice == 1:
        print(paper)
    if yourChoice == 2:
        print(scissors)

    compChoice = random.randint(0, 2)
    print("Computer Choice is:")
    if compChoice == 0:
        print(rock)
    if compChoice == 1:
        print(paper)
    if compChoice == 2:
        print(scissors)

    GameWin(yourChoice, compChoice)
    a = 0
    while a != 'yes' or a != 'yes':
        a = input("Type Yes to continue the game and q to quit: ")
        if a == 'Yes' or a == 'yes':
            pass
        elif a == 'q' or a == 'Q':
            exit()
        else:
            print("invalid choice!")
