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

choice= int(input("What do you choose (1,2 or 3)?\n1. Rock\n2. Paper\n3. Scisso\nr"))
y=random.randint(1,3)
if choice==1:
    print(rock)
    if y==1:
        print(rock)
        print("Draw")
    elif y==2:
        print(paper)
        print("You Lose")
    elif y==3:
        print(scissors)
        print("You Won")
elif choice==2:
    print(2)
    if y==1:
        print(rock)
        print("You Won")
    elif y==2:
        print(paper)
        print("Draw")
    elif y==3:
        print(scissors)
        print("You Lose")
elif choice==3:
    print(3)
    if y==1:
        print(rock)
        print("You Lose")
    elif y==2:
        print(paper)
        print("You Win")
    elif y==3:
        print(scissors)
        print("Draw")
