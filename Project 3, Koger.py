#Hailey Koger, CMSC 210, 3/02/2021, Project 3

#asking teller to enter the number of coins

quarters = eval(input("How many quarters? "))

dimes = eval(input("How many dimes? "))

nickles = eval(input("How many nickels? "))

pennies = eval(input("How many pennies? "))

#verifying the amount of coins that they have entered

print ( "You have entered",quarters,"quarters", '\n', "You have entered",dimes, "dimes", "\n", "You have entered",nickles, "nickles", "\n", "You have entered",pennies, "pennies")

#now verfying they have put the correct number of coins in

answer = str(input("Is this correct? "))

# defining combine with the math of additon for thier total number of coins

combine =(0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)



#The ifelse statement to the question that was just asked to the user

if answer.lower() == ("yes"):
    
    print ("Your total monies is", "{:.2f}".format(combine)) #my print statement telling them what their total is by calling the variable ,combine,

#because the user entered something other than Yes/yes the user is being asked again to enter the amount of coins they have
else:
        
    quarters = eval(input("How many quarters? "))

    dimes = eval(input("How many dimes? "))

    nickles = eval(input("How many nickels? "))

    pennies = eval(input("How many pennies? "))

    print ( "You have entered",quarters,"quarters", '\n', "You have entered",dimes, "dimes", "\n", "You have entered",nickles, "nickles", "\n", "You have entered",pennies, "pennies")

    combine = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)

    print ("Your total monies is", combine )

yeNo = str(input("Are you done?")

print (yeNo);
