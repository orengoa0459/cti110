# This program converts Kilometers to miles
# 7/02/2019
# CTI-110 P5T1_KilometerConverter 
# Anthony Orengo


# 1.) Create two funtions called main() and miles().
#
# 2.) Declare variables
#     kilometers = float 0.0
#     kilometer_Conversion = .6214
#
# 3.) Prompt user to input number of kilometers in function main().

# 4.) Calculate kilometers to miles in function miles() using formula.
#     miles = km * kilometer_Conversion
#
# 5.) Display distance in miles.

# Declare variables.
kilometer_Conversion = .6214
kilometers = 0.0


def main():
    # Prompt user to input distance in kilometers.
    kilometers = float(input("Enter a distance in kilometers:  "))

    # Display converted distance in miles.
    miles(kilometers)

def miles(km):
    # Formula for kilometer convertion.
    miles = km * kilometer_Conversion

    # Display distance in miles.
    print(km, "kilometers equals ", miles, "miles")
# Call the main function. 
main()
