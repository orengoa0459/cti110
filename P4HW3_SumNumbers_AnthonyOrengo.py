# This program calculates the sum of positive numbers. 
# 06/30/2019
# CTI-110 P4HW3 - Sum of Numbers
# Anthony Orengo
#

# 1.) Define function as main().
# 2.) Declare variables.           
#           total = float 0.0
#           num = float 0.0
# 3.) Create while loop keep_going
#
# 4.) Prompt user to input positive numbers.
# 5.) If user enters a negative number, stop loop and add the positve numbers.
#           a. total = total + num
# 6.) Display sum of positive numbers.



def main():

    # Initialize  accumulator.
    total = 0.0
    num = 0.0
    keep_going = 'y'

    # Initiate while loop
    while keep_going== 'y':
        # Prompt user to input positive numbers.
        num = float(input("Enter a positve number: "))
        # If user enters a positive the loop will continue.
        if num > 0:
            print("Enter another positive number or enter a negative number to end: ")
            total = total + num

        else:
            # If user inputs a negative number display sum of positive numbers.
            print("The total sum of positive numbers is:", total)
            keep_going = 'n'

main()
            
  
      
