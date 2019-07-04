# Lab 4.6 Programming Challenge 1 - Tip, Tax,and Total

def main():
    mealPrice = getMeal()
    calcTip = getTips(mealPrice)
    calcTax = getTax(mealPrice)
    calcTotal = getTotal(mealPrice,calcTip, calcTax)
    printValues(mealPrice, calcTip, calcTax, calcTotal)


def getMeal():
    mealPrice = float(input('Enter the meal price $'))
    mealPrice = float(mealPrice)
    return mealPrice


def getTips(mealPrice):
    if mealPrice >= 0.01 and mealPrice <= 5.99:
        calcTip = mealPrice * 0.1
    elif mealPrice >= 6 and mealPrice <= 12.00:
        calcTip = mealPrice * 0.13
    elif mealPrice >= 12.01 and mealPrice <= 17.00:
        calcTip = mealPrice * 0.16
    elif mealPrice >= 17.01 and mealPrice <= 25.00:
        calcTip = mealPrice * 0.19
    else:
        calcTip = mealPrice * 0.22
    return calcTip


def getTax(mealPrice):
    calcTax = mealPrice * 0.06
    return calcTax

def getTotal(mealPrice, calcTip, calcTax):
    calcTotal = mealPrice + calcTip + calcTax
    return calcTotal

def printValues(mealPrice, calcTip, calcTax, calcTotal):
    print('The meal Price is $ ', mealPrice)
    print('The tip is $ ', calcTip)
    print('The tax is $ ', calcTax)
    print('The total is $ ', calcTotal)



main()