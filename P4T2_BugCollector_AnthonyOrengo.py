# This program calculates the number of bugs collected for five days.
# 07/02/2019
# CTI-110 P4T2 - Bug Collector
# Anthony Orengo

# 1.) Define function as main().
# 2.) Set accumulator to total = 0.
#    
# 3.) Create controlled loop "day".
#     a. Set range to (1, 6)
# 4.) Prompt user to input number of bugs collected for days 1 - 5).
# 5.) Calculate total number of bugs collected.
#     a. total += bugs
# 6.) Display number of bugs collected.


#Define function as main().
def main():
    # Initialize  accumulator.
    total = 0

    # Count controlled loop.  
    for day in range(1, 6):
        print('Enter number of bugs collected on day', day)
        #Prompt user to input number of bugs collected.
        bugs = int(input())
        #Calculate total number of bugs collected.
        total += bugs

    #Display the total number of bugs collected after five days.
    print('You collected a total of', total, 'bugs.')

    
main()
