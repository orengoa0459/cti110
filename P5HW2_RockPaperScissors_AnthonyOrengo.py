# This program is a version of the game rock, paper, scissors.
# 07/04/2019
# CTI-110 P5HW2_RockPaperScissors 
# Anthony Orengo
#
# 1.) Create funtion called main()
# 2.) Import random module
#     create funtion called number = random.randint(1, 3)          
#
# 3.) Declare variables
#     rock = "Rock"
#     paper = "Paper"
#     scissors = "Scissors"
#
# 4.) Prompt player 1 to type Rock, Paper, or Scissors (may use upper or lower case letters). 
#
# 5.) Create arguments to determine winner/loser, and rematch/draw. 
#
# 6.) Display results of winner and loser.
# 7.) If match is a draw, restart main function.

# Declare variables.

# Loads contents of the random module.
import random
# Function call with argument. Generates a random integer 1-3.
number = random.randint(1, 3)

# Declare variables
rock = "Rock"
paper = "Paper"
scissors = "Scissors"

# Creates an extra space.
x=' ';

# Define function as main().
def main():

    # Prompt player 1 to enter Rock, Paper, or Scissors.
    # May use upper or lower case letters. 
    user_choice = str(input("Player 1 Enter Rock, Paper, or Scissors: ").lower())
    
    # Argument determining which player won.
    # Diplay results of winner.
    if number == 1 and user_choice == "scissors":
        print("Player 2 chose Rock")
        print(2*x); # Adds 2 spaces
        print("Player 1 you lose.")
        print("Player 2 you win.")
    elif number == 3 and user_choice == "rock":
        print("Player 2 chose Scissors")
        print(2*x);
        print("Player 1 you win.")
        print("Player 2 you lose.")

    elif number == 1 and user_choice == "paper":
        print("Player 2 chose Rock")
        print(2*x);
        print("Player 1 you win.")
        print("Player 2 you lose.")
    elif number == 2 and user_choice == "rock":
        print("Player 2 chose Paper")
        print(2*x);
        print("player 1 you lose.")
        print("Player 2 you win.")

    elif number == 2 and user_choice =="scissors":
        print("Player 2 chose Paper")
        print(2*x);
        print("player 1 you win.")
        print("Player 2 you lose.")
    elif number == 3 and user_choice == "paper":
        print("Player 2 chose Scissors")
        print(2*x);
        print("player 1 you lose.")
        print("Player 2 you win.")

        # Argument for draw and rematch.
        # Redirect back to main function for rematch.
    elif number == 1 and user_choice == "rock":
        print("Player 2 chose Rock")
        print(2*x);
        print("Draw! Rematch.")
        main()
    elif number == 2 and user_choice == "paper":
        print("Player 2 chose Paper")
        print(2*x);
        print("Draw! Rematch.")
        main()
    elif number == 3 and user_choice == "scissors":
        print("Player 2 chose Scissors")
        print(2*x);
        print("Draw! Rematch.")
        main()
# Call the main function
main()



    
    
    
