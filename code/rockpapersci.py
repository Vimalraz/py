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
---'    ____)____
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
random_list = ["r", "p", "s"]
user_compare = ""
computer_compare = ""

#user_choosing
user_choice = input("Choose Rock, Paper or Scissor by typing R,P,S: \n").lower()
if user_choice == 'r':
    print(rock)
    user_compare = 0
elif user_choice == 'p':
    print(paper)
    user_compare = 1
elif user_choice == 's':
    print(scissors)
    user_compare = 2
else:
    print("You have enterd wrong input, Please try again!\n")

#computer choice
computer_choice = random.choice(random_list)
if user_choice == "r" or user_choice == "p" or user_choice == "s":
    print("Computer chose:")
    if computer_choice == 'r':
        print(rock)
        computer_compare = 0
    elif computer_choice == 'p':
        print(paper)
        computer_compare = 1
    elif computer_choice == 's':
        print(scissors)
        computer_compare = 2
    
#who won - new
if user_choice == "r" or user_choice == "p" or user_choice == "s":
    #same choice draw
    if user_compare == computer_compare:
        print("Draw")
    elif user_compare == 0 and computer_compare == 2:
        print("You Win")
    elif computer_compare == 0 and user_compare == 2:
        print("You Lose")
    elif user_compare > computer_compare:
        print("You Win")
    elif computer_compare > user_compare:
        print("You Lose")

# #deciding who won_my own idea - not very optimized for cases
# if user_choice == "r" or user_choice == "p" or user_choice == "s":
#     #same choice draw
#     if user_compare == computer_compare:
#         print("Draw")
#     elif user_compare == 1 or computer_compare == 1:
#         if user_compare > computer_compare:
#             print("You Win")
#         else:
#             print("You lose")
#     elif user_compare == 2 or computer_compare == 2:
#         if user_compare == 0:
#             print("You Win")
#         elif computer_compare == 0:
#             Print("You lose")
#         if user_compare == 1:
#             print("You lose")
#         elif computer_compare == 1:
#             print("You Win")

#rock defeats scissor
#scissor defeats paper
#paper defeats rock

