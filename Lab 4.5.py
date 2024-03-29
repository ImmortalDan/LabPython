# Dan Munene
# 7/4/2019
# This program illustrates if else statements
# Lab 4.5
# The main function

def main():
    monthlySales = getSales() # call to get sales
    salesIncrease = getIncrease()  # call to get sales increase
    storeAmount = storeBonus(monthlySales)
    empAmount = empBonus(salesIncrease)
    printBonus(storeAmount, empAmount)


# This function gets the monthly sales
def getSales():
    monthlySales = float(input("Enter the monthly sales $"))
    return monthlySales


# This function gets the percent of increase in sales
def getIncrease():
    salesIncrease = float(input('Enter percent of sales increase: '))
    salesIncrease = float(salesIncrease)
    salesIncrease = salesIncrease / 100
    return salesIncrease

# This function determines the storeAmount bonus
def storeBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 3000
    else:
        storeAmount = 0
    return storeAmount

# This function determines the empAmount bonus
def empBonus(salesIncrease):
    if salesIncrease >= 0.05:
        empAmount = 75
    elif salesIncrease >= 0.04:
        empAmount = 50
    elif salesIncrease >= 0.03:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount

# This function prints the bonus information
def printBonus(storeAmount, empAmount):
    print("The store bonus is $ ", storeAmount)
    print('The employee bonus is $ ', empAmount)
    if storeAmount == 6000 and empAmount == 75:
        print('Congrats! You have reached the highest bonus amounts possible!')



# calls main function
main()




