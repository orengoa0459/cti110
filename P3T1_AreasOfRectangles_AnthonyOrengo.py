# This program calculates the area of two rectangles and determines whether they
# are greater than or equal to each other.

# 6/18/2019
# CTI-110 P3T1-Areas of Rectangles
# Anthony Orengo

# Pseudocode 
# 1.) Define main function as main().
# 2.) Declare variables
#       rectangleOneLength = 0.0 float 
#       rectangleOneWidth = 0.0 float 
#       rectangleTwoLength = 0.0 float 
#       rectangleTwoWidth = 0.0 float 
#       rectangleOneArea = 0.0 float
#       rectangleTwoArea = 0.0 float
# 3.) Prompt user to input length and width for rectangle one and two.
# 4.) Calculate the area of both rectangles using the following formula.
#       area = length * width
# 5.) Display the area of both rectangles.
# 6.) Set "if" function to determine which rectangle is larger or is both are equal to each other.
# 7.) Display which rectangle is larger or if they are both equal.
# 8.) Return to main function. 

# Define function as main()
def main():
    # Prompt user to input length and width for each rectangle
    rectangleOneLength = float(input(" Enter rectangle 1's length:  "))
    rectangleOneWidth = float(input(" Enter rectangle 1's width:  "))

                                 
    rectangleTwoLength = float(input(" Enter rectangle 2's length:  "))
    rectangleTwoWidth = float(input(" Enter rectangle 2's width:  "))
    # Calculate area of rectangle one by multiplying length and width
    rectangleOneArea = rectangleOneLength * rectangleOneWidth

    # Calculate area of rectangle two by multiplying length and width
    rectangleTwoArea = rectangleTwoLength * rectangleTwoWidth

    # Display results of rectangle one and two
    print( " The area of rectangle one is:  ", rectangleOneArea)
    print( " The area of rectangle two is:  ", rectangleTwoArea)

    # If statement comparing which rectangle is larger or if both are equal
    # Display results of larger rectangle or if both are equal
    if rectangleOneArea > rectangleTwoArea:
    
        print("Rectangle one is larger.")
    else:    
      
         if rectangleTwoArea > rectangleOneArea:
            print("Rectangle two is larger.")
         else:
               if rectangleOneArea == rectangleTwoArea:
                    print("Both rectangles have equal area.")
    # Return to main statement
    return main()

# Start of main function.
main()

                
