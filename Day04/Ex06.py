# rock , paper and scissor 
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
scissor='''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''


print("Welcome TO Rock Paper and Scissor Game\n")
user_input=int(input("Enter 0 for Rock , 1 for paper and 2 for scissor\n"))
computer_input=random.randint(0,2)

if user_input==0:
    print(f"Your choice \n {rock}")
elif user_input==1:
    print(f"Your choice \n {paper}")
elif user_input==2:
    print(f"Your choice \n {scissor}")
else:
    print("\n Invalid input !!! you have to choose between 0 ,1 and 2")
    

if computer_input==0:
    print(f"Computer Choice \n {rock}")
elif  computer_input==1:
    print(f"Computer Choice \n {paper}")
elif  computer_input==2:
    print(f"Computer Choice \n {scissor}")


if user_input==0 and computer_input==1:
    print("Congo !!! YOU WIN")
elif user_input==1 and computer_input==2:
    print("BUDDY!!! YOU LOOSe")
elif user_input==2 and computer_input==0:
    print("BUDDY!!! YOU LOOSe")
elif computer_input==0 and user_input==1:
    print("BUDDY!!! YOU LOOSe")
elif computer_input==1 and user_input==2:
    print("Congo !!! YOU WIN")
else:
    print("Match Draw !!! Try Another Time \n Thank YOU")



