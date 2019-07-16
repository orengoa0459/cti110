# This program displays a pounds to kilograms table.
# 06/30/2019
# CTI-110 P4HW2 - Pounds to Kilos Table
# Anthony Orengo


# 1.) Define function as mainBug()
# 2.) Declare variables.
#       kgs = float 2.2046           
#       convertion = num / kgs
#       end = str
# 3.) Create loop for "num" in range (100, 310, 10).
# 4.) Calculate pounds to kgs using the following formula.
#       convertion = num / kgs
# 5.) Display results.


def main():
      
    # Loop for "num" in range (100, 310, 10).
    for num in range(100, 310, 10):
        # Calculate pounds to kgs.
        kgs = 2.2046
        convertion = num / kgs   
    
    #   Display number of pounds, upto 310lbs, converted to kgs.
        print(num, "lbs", "Equals:",  convertion, "kg")
      
main()


    

    

