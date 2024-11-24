rock = '''
    _______
---'   ____)
      (_)
      (_)
      ()
---.(_)
'''

paper = '''
    _______
---'   ___)___
          ______)
          _______)
         _______)
---.)
'''

scissors = '''
    _______
---'   ___)___
          ______)
       __________)
      ()
---.(_)
'''

import random
comp_opt = random.randint(1,3)
opt = int(input("Welcome to Rock, Paper and Scissors game.\nYour Turn.\nChoose 1 for rock, 2 for paper and 3 for scissors!\n"))
if(opt==1):
    print(f"You chose rock.\n{rock}")
    comp_opt = random.randint(1,3)
    if(comp_opt==1):
        print(f"computer chose rock.\n{rock}\n\nDraw, play again.")
    elif(comp_opt==2):
        print(f"computer chose paper.\n{paper}\n\nPaper covers rock, you lose!")
    else:
        print(f"computer chose scissors.\n{scissors}\n\nRock crushes scissors, You win!")
elif(opt==2):
    print(f"You chose paper.\n{paper}")
    comp_opt = random.randint(1,3)
    if(comp_opt==1):
        print(f"computer chose rock.\n{rock}\n\nPaper covers rock, You win!")
    elif(comp_opt==2):
        print(f"computer chose paper.\n{paper}\n\nDraw, play again.")
    else:
        print(f"computer chose scissors.\n{scissors}\n\nScissors cuts paper, You lose!")
else:
    print(f"You chose scissors.\n{scissors}")
    comp_opt = random.randint(1,3)
    if(comp_opt==1):
        print(f"computer chose rock.\n{rock}\n\nRock crushes scissors, You lose!")
    elif(comp_opt==2):
        print(f"computer chose paper.\n{paper}\n\nScissors cuts paper, You win!")
    else:
        print(f"computer chose scissors.\n{scissors}\n\nDraw,play again")