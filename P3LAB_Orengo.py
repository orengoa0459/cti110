# This program determines the letter grade for the 10-point grading scale
# CTI-110
# P3LAB  
# Anthony Orengo
# 06/18/2019


# 1.) Define function as main()
# 2.) Declare variables
#      score = float 0.0
#      A_score = float 90.0
#      B_score = float 80.0
#      C_score = float 70.0
#      D_score = float 60.0
#      F_score = float 50.0

# 3.) Prompt user to input a number
# 4.) Determine letter grade for users input
# 5.) Display users letter grade


# Define function as main().
def main():    

    # System uses 10-point grading scale.
    A_score = 90.0
    B_score = 80.0
    C_score = 70.0
    D_score = 60.0
    F_score = 50.0
    

    #Prompt user to input number grade.
    score = float(input("Enter grade: "))

    # Determine which letter grade the users number is.
    # Display users letter grade.
    if score >= A_score:
        print('Your grade is: A')
    elif score >= B_score:
        print('Your grade is: B')
    elif score >= C_score:
        print('Your grade is a: C')
    elif score >= D_score:
        print('Your grade is a: D')
    elif score >= F_score or score <= F_score:
        print('Your grade is: F')
      

    return main()


# Main function starts. 
main()
