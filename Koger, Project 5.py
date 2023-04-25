
#Hailey Koger, 04/05/2021, CMSC210, Project 210

#Starting with setting the controls to 0, and writing my input that will be asked
numEntry = 0
totalAns = 0
ans = eval(input("Please rate the library service from 0 (completely unsatisfactory) to 4 (outstanding): "))
#starting the while loop
while ans != -999:
    if ans >= 0 and ans <= 4: #using this to make sure that invlaid number responses will not be recorded when the average is given later
        totalAns = totalAns + ans #making sure their valid response is added up
        numEntry = numEntry + 1 #keeping count of the valid responses
    else:
        print ("This entry is invalid") #letting user know that their number was invalid and then below asking them again for a response
    ans = eval(input("Please rate the library service from 0 (completely unsatisfactory) to 4 (outstanding): "))
xy = totalAns / numEntry #setting the equation to a variable to make it easy to call it if the program ever needs anything extra
print ("Average is " + str(xy)) #what will happen when -999 is entered and the loop breaks, the user will get the average





    
    

        
