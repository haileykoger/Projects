#Hailey Koger, CMSC 210, Project 7, 04/28/21

def bonusQues(yearsSales, yearsofService):
    monthlyAveSales = yearSales / 12
    if monthlyAveSales < 1000:
        salesBonus = 100
    elif monthlyAveSales >= 1000 and monthlyAveSales < 2000:
        salesBonus = 200
    elif monthlyAveSales >= 2000 and monthlyAveSales < 3000:
        salesBonus = 300
    else:
        salesBonus = 400
    if yearsOfService >= 20:
        totalBonus = salesBonus * 1.20
    elif yearsOfService >= 10:
        totalBonus = salesBonus * 1.10
    else:
        totalBonus = salesBonus
        
    return(totalBonus)

yearsSales = float(input("How much for the year did the employee make in sales?: "))
yearsOfService = int(input("How many years with the company does the employee have? :"))

print ("The total bonus is" + str(totalBonus))
