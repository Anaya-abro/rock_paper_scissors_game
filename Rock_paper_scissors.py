import random

print("🎉Welcome to Rock paper scissors game🎊")

computer = ['rock','paper','scissors']

while True:
 computer_choice = random.choice(computer)
 user_input = input("What do you want to choose(Rock🪨/Paper📃/Scissors✂️):").lower()

# user win 

 if user_input == computer_choice:
    print(f"|You chose {user_input}| and |computer chose {computer_choice}|")
    print('GAME TIE')

 elif user_input == 'rock' and computer_choice == 'scissors':
    print(f"|You chose {user_input}| and |computer chose {computer_choice}|")
    print("YOU WIN🎉")

 elif user_input == "paper" and computer_choice == 'rock':
    print(f"|You chose {user_input}| and |computer chose {computer_choice}|")
    print("YOU WIN🎉")


 elif user_input == 'scissors' and computer_choice == 'paper':
    print(f"|You chose {user_input}| and |computer chose {computer_choice}|")
    print("YOU WIN🎉")


# computer win 

 elif computer_choice == 'rock' and user_input == 'scissors':
    print(f"|You chose {user_input}| and |computer chose {computer_choice}|")
    print("Computer win!")


 elif computer_choice == 'paper' and user_input == 'rock':
    print(f"|You chose {user_input}| and |computer chose {computer_choice}|")
    print("Computer win!")


 elif computer_choice == 'scissors' and user_input == 'paper':
    print(f"|You chose {user_input}| and |computer chose {computer_choice}|")
    print("Computer win!")


 else:
    print('invalid text')
    
    























































































