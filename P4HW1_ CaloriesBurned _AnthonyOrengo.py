# This program calculates total calories burned. 
# 06/30/2019
# CTI-110 P4HW1 - Calories Burned
# Anthony Orengo


# 1.) Define function as main().
# 2.) Declare variables.
#           calories = float 0.0
#           time = float 0.0
#           total_calories = float 0.0
# 3.) Prompt user to input number of calories burned per minute.
# 4.) Calculate number of calories burned after 25,35,and 45 minutes of exercise.
#           a.) Create loop for "time" (25, 35, 45).
#           b.) formula: total_calories = time * calories
# 5.) Display total calories burned for 25, 35, 45 minutes of exercise.


# Define function as main().
def main():
    
    # Prompt user to input number of calories burned per min.
    calories = float(input("Enter number of calories your body burns per min:  "))  

    
    # Loop for "time" (25, 35, 45).
    for time in range(25, 46 , 10):
        # Calculate number of calories burned after 25, 35, and 45 minutes of exercise.
        total_calories = time * calories
        # Display total calories burned for 25, 35, 45 minutes of exercise.
        print(time, "Minutes", "=", total_calories,  "Total calories burned")

# Main function   
main()
