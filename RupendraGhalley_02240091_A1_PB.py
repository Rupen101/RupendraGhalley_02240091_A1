
import random

def guess_number_game():
       
       lower_number = 1
       upper_number= 100
       comp = random.randint(lower_number , upper_number)
       print(f"Welcome to the Guess Game.")
       print(f"Guess the number between 1 and 100.")
       attempts = 0
       
       while True :
           attempts += 1
           user_input = int(input("Enter your Guess: "))
           if user_input < comp :
                 print("go higher ")
           elif user_input > comp :
                 print("go lower ")
           else:
                 print("congratulation !! YOU WON ")
                 break
       print (f"you have attempted {attempts}")
# guess_number_game()     



import random
input_option = ("Rock", "Paper", "Scissor")
def Rock_Paper_Scissor():
      while True:

            player = None
            computer = random.choice(input_option)
            while player not in input_option:
                  player = input("enter your choice from option(Rock,Paper,Scissor): ")
            print(f"player: {player}")
            print(f"Computer: {computer}")

            if player == computer:
                  print("Draw")
            elif player == "rock" and computer == "scissor":
                  print("You win")

            elif player == "Scissor" and computer == "Paper":
                  print("you win")

            elif player == "Paper" and computer == "Rock":
                  print("You win")
            else:
                  print("You lose")
            print("Thank you")

            play_again = input("Do you want to Play again? (yes/no: ").lower()
            if not play_again == "yes":
                  running = False

            print("Thank you for playing")

while True:
    print("Menu ")
    print("1. Guess Game")
    print("2. Rock,Paper,Scissor")
    print("3. Exit")
    
    choice = input("select an option (1-3): ")
    if choice == '1':
          guess_number_game()
    elif choice == '2': 
          Rock_Paper_Scissor()
    elif choice == "3": 
          break
    
        

            
    
