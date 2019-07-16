# This program will determine the secondary color.
# CTI-110 
# P3HW1 - Color Mixer 
# Anthony Orengo
# 06/18/2019

# Pseudocode 
# 1.) Define main function as colorMain().
# 2.)Display color options menu with print function.
#      print("Red") 
#      print("Yellow") 
#      print("Blue") 
#
# 3.) Declare color variables
#      red = str "red"
#      yellow = str "yellow"
#      blue = str "blue"
#      color_one = str
#      color_two = str
#
# 4.) Prompt user to input two colors.
# 5.) Determine secondary color based on users color options.
#      a.) Set "if" statement to calculate secondary color.
#      b.) Set "else:" "if", for same color chosen if users fails to pick two different colors.
#      c.) Set "else:" "if", for "invalid selection" if user fails to choose one of the color options listed.
# 6.) Display results of secondary color.
# 7.) Return statement for colorMain()


# Define function as colorMain.
def colorMain():    
       print("Color Option Menu")
       print("Red:")
       print("Yellow:")
       print("Blue:")


       # Color variables
       red = "red"
       yellow = "yellow"
       blue = "blue"
       
       # Prompt user to input two colors
       color_one = str(input(" Enter your first primary color:  "))
       color_two = str(input(" Enter your second primary color:  "))

       # Determine secondary color based on users color options.
       # If statement representing argument between two colors.
       if color_one == "red" and color_two == "blue" or color_two == "red" and color_one == "blue":
              print("Your color is: Purple")

       else:
           if color_one == "red" and color_two == "yellow" or color_two == "red" and color_one == "yellow":
               print("Your color is: Orange")
           else:
                if color_one == "yellow" and color_two == "blue" or color_two == "yellow" and color_one == "blue":
                     print("Your color is: Green")
                     
                else:# else if users fails to pick two different colors.                     

                       if color_one == "red" and color_two == "red" or color_two == "red" and color_one == "red":
                              print("The color mixer program determines secondary colors only.")
                              print("The program will entertain your choices.")
                              print("Your color is: Red")
                       else:
                              if color_one == "yellow" and color_two == "yellow" or color_two == "yellow" and color_one == "yellow":
                                     print("The color mixer program determines secondary colors only.")                                           
                                     print("The program will entertain your choices.")
                                     print("Your color is: Yellow")
                              else:
                                     if color_one == "blue" and color_two == "blue" or color_two == "blue"  and color_one == "blue" :
                                            print("The color mixer program determines secondary colors only.")
                                            print("The program will entertain your choices.")
                                            print("Your color is: Blue")
                                     
                                     else: # else if user fails to choose one of the color options listed.
                                            print("Invalid selection")
       # return to colorMain after selection
       return colorMain()
# Start of main function.
colorMain()



