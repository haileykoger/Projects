#Hailey Koger, CMSC 210, 03/21/2021, Project 4
#asking user to input the needed information
fname = input('First Name: ')
lname = input('Last Name: ')
nyear = eval(input('Numeber of years with the company: '))
yyear = eval(input('Total sales for the year in dollars: '))

#now reporting the amount of totale sales in the year for said person

print (fname + ' ' + lname + '\'s total sales for the year are' + ' ' + '$' + str(yyear))

#now need to divide yyear by 2 to get monthly sales amount
msa = yyear / 12

print (fname + ' ' + lname + '\'s monthly sale average is' + ' ' + '$',round(msa))

#Now using nested if's for the caculations and summary of bonuses

if msa < 1000:
    print(fname + ' ' + lname + '\'s bonus is $100')
    if nyear >= 20:
        print ('Because of more than 20 years of service'+ ' ' + fname + ' ' + lname + '\'s bonus will be a total of $',100 + 100 * 0.2)
    elif nyear >= 10 and nyear < 20:
             print ('Because of 10 to 20 years of service' + ' ' + fname + ' ' + lname + '\'s bonus is $', 100 + 100 * 0.1)
    else:
        print(fname + ' ' + lname + '\'s bonus stays at $100 because there is less than 10 years of service with the company.')
if msa >= 1000 and msa < 2000:
    print(fname + ' ' + lname + '\'s bonus is $200')
    if nyear >= 20:
        print ('Because of more than 20 years of service' + ' ' + fname + ' ' + lname +'\s bonus will be a total of $', 200 + 200 * 0.2)
    elif nyear >= 10 and nyear < 20:
        print('Because of 10 to 20 years of service'+ ' ' + fname + ' ' + lname + ' ' + '\'s bonus is $', 200 + 200 * 0.1)
    else:
        print(fname + ' ' + lname + '\'s bonus stays at $200 because there is less than 10 years of service with the company.')
        
if msa >= 2000 and msa < 3000:
    print(fname + ' ' + lname + '\'s bonus is $300')
    if nyear >= 20:
        print ('Because of more than 20 years of service' + ' ' + fname + ' ' + lname +'\s bonus will be a total of $', 300 + 300 * 0.2)
    elif nyear >= 10 and nyear < 20:
        print('Because of 10 to 20 years of service'+ ' ' + fname + ' ' + lname + ' ' + '\'s bonus is $', 300 + 300 * 0.1)
    else:
        print(fname + ' ' + lname + '\'s bonus stays at $300 because there is less than 10 years of service with the company.')
    
if msa >= 3000:
    print(fname + ' ' + lname + '\'s bonus is $400')
    if nyear >= 20:
        print ('Because of more than 20 years of service' + ' ' + fname + ' ' + lname +'\s bonus will be a total of $', 400 + 400 * 0.2)
    elif nyear >= 10 and nyear < 20:
        print('Because of 10 to 20 years of service'+ ' ' + fname + ' ' + lname + ' ' + '\'s bonus is $', 400 + 400 * 0.1)
    else:
        print(fname + ' ' + lname + '\'s bonus stays at $400 because there is less than 10 years of service with the company.')
