# Guess the random number
# 7/02/2019
# CTI-110 P5HW1 - Random Number 
# Anthony Orengo


# 1.) Import random and set boundaries.
#       number = random.randint(1, 100)
# 2.) Declare variables
#     guess = 'y'    
#     count = 0
# 3.) Create while loop called "guess"
#     guess == 'y'
#
# 3.) Prompt user to input a number.

# 4.) Create argument for user input.
#     if users guess is to high or to low restart loop
#     If user guess right stop the loop.
#
# 5.) Display results and number of attempts.

# Loads contents of the random module.
import random
# Function call with argument. Generates random number 1-100.
number = random.randint(1, 100)

# Argument for while loop.    
guess = 'y'

# Count variable for number of attempts.
count = 0

# Loop begins.
while guess == 'y':
    # Initiate counter for number of attempts.
    count +=1
    # Prompt user to guess random number.
    # Continue loop until user guesses the correct random number.
    user_num = int(input("Guess the random number:  "))
    
    if user_num > number: 
            print("Too high, try again")
          
    elif user_num < number:
            print("Too low, try again")
                  
    else:
        if user_num == number:
            # If user guess correctly display results and number of attempts.
            print("Congratulations! You guessed right the correct number.")
            print("Number of Attempts: ", count)
            guess = 'n'



