# This program calculates feet to inches
# 07/04/2019
# CTI-110 P5T2_FeetToInches 
# Anthony Orengo
#
# 1.) Create two funtions called main() and feet_to_inches(feet).
#
# 2.) Declare variables
#     feet = float 0.0
#     inches = 12
#
# 3.) In function main(), prompt user to input number of feet. 
#
# 4.) Calculate feet to inches in function feet_to_inches(feet) using:
#     return feet * inches
#
# 5.) In function main() print results.

# Declare variables.

feet = 0.0
inches = 12

# Main function.
def main():
    # Prompt user to input number of feet.
    feet = float(input("Enter total number of feet:  "))

    # Display converted feet to inches.
    print(feet, 'feet equals', feet_to_inches(feet), 'inches.')

# feet_to_inches function.
def feet_to_inches(feet):

    return feet * inches

# Call the main function.
main()
