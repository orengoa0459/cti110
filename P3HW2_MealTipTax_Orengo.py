# This program determines total meal cost including tax and tip. 
# CTI-110 
# P3HW2 - MealTipTax 
# Anthony Orengo
# 06/18/2019

# Pseudocode 
# 1.) Define function as main().
# 2.) Declare set one variables
#        tip_15 = float .15
#        tip_18 = float .18
#        tip_20 = float .20
#        tax = float .07
#        meal_cost = float 0.0
#        meal_tax = meal_cost * tax 
#
# 3.) Prompt user to enter cost of meal.
# 4.) Calculate meal_tax by multiplying variables meal_cost and tax.  
# 4.) Print display for user tip options.
#            print 15%,
#            print 18%
#            print 20%
# 5.) Prompt user to input tip percentage.
# 6.)  Set total tip cost to variables.
#    **Declare set two variables.
#        meal_tip
#        total_15 = tip_15 * meal_cost
#        total_18 = tip_18 * meal_cost
#        total_20 = tip_20 * meal_cost
# 7.) Calculate tip cost by multiplying meal_cost by meal_tip.
# 8.) Set "if" statement for users tip option.
#       ex. if meal_tip == 15
#       print("Your total meal cost is:")
#       print("Meal Cost:", meal_cost)
#       print("Meal tip:", total_15)
#       print("Meal tax:", meal_tax)
#       print("Total meal cost:", meal_cost + meal_tax + total_15)
#       repeat for each percentage using "elif".
#       End statement with
#       else:
#       print("Error! Invalid tip percentage")
# 9.) Display results from if statement.
# 10.) return to main()

# Define function as main()
def main():
    # Meal tip variables
    tip_15 = .15 
    tip_18 = .18
    tip_20 = .20

    # Tax variable
    tax = .07
    

    # Prompt user to input cost of meal
    meal_cost = float(input(" Enter your meal cost:  "))

    # Meal tax variable
    meal_tax = meal_cost * tax
    
    # Display menu representing user options for 15%, 18%, 20%
    print("Meal tip options")
    print("15%")
    print("18%")
    print("20%")
    
    # Prompt user to input tip percentage
    meal_tip = float(input("Choose your gratuity:  "))

    # Total meal tip cost variables
    total_15 = tip_15 * meal_cost
    total_18 = tip_18 * meal_cost
    total_20 = tip_20 * meal_cost
    
 
    # "if" statement for users tip option.
    # Print total meal cost with tax and tip included.
    if meal_tip == 15:
        print("Your total meal cost is:")
        print("Meal Cost: $" + str(meal_cost))
        print("Meal tip: $" + str(total_15))
        print("Meal tax: $" + str(meal_tax))
        print("Total meal cost: $" + str(meal_cost + meal_tax + total_15))
    elif meal_tip == 18:
        print("Your total meal cost is:")
        print("Meal Cost: $" + str(meal_cost))
        print("Meal tip: $" + str(total_18))
        print("Meal tax: $" + str(meal_tax))
        print("Total meal cost: $" + str(meal_cost + meal_tax + total_18))
    elif meal_tip == 20:
        print("Your total meal cost is:")
        print("Meal Cost: $" + str(meal_cost))
        print("Meal tip: $" + str(total_20))
        print("Meal tax: $" + str(meal_tax))
        print("Total meal cost: $" + str(meal_cost + meal_tax + total_20))
    # set invalid if user fails to chose the tip options listed.    
    else:
        print("Error! Invalid tip percentage")
                
    # Return to main statement (restart program)
    return main()

# Start of main function.
main()
