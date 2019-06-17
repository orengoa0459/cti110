
# Calculates projected annual profits.
# 6/12/2019
# CTI-110 P2T1-Sales Prediction
# Anthony Orengo

# Create function by defining main.
# Prompt user to input projected amount of total sales.
# Set projected annual sales to variable "projected_sales".
# Set typical annual profit percentage to variable "percent".
# Set total profits to variable "total".
# Calculate annual profits by variable "projected sales" and variable "percent"
# Display annual profits in a print statement. 
# Create "return" statement and input "main()".
# Initiate program by defining "main" function.


# Define "main()" as a function for Sales Prediction.
def main():
    # Prompt user to input projected annual sales.
    projected_sales = float(input("Enter your projected amount of total sales: "))

    # Variable represents the typical annual profit percentage.
    percent = .23
    
    # Calculate annual profits by variable "projected sales" and variable "percent".
    total = percent * projected_sales

    # Print results of percent multiplied by projected total sales.
    #
    # "str" added for character "$" placement. Note: will change data variables to string format.
    # remove "str" and replace "+" with  "," to return string to data.
    print('Your projected annual profit is $' + str(total))

    # Return statement
    return main()
    
main()






