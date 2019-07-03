# lab 2.7 Programming Challenge 1- Retail Tax

def main():
    print('Welcome to the retail tax calculator')
    print()

    totalsales = inputData()
    countytax = calcCounty(totalsales)
    statetax = calcState(totalsales)
    total = calcTotal(countytax, statetax)
    printData(total, countytax, statetax)




def inputData():
    totalsales = input('Enter the total sales for the month')
    totalsales = float(totalsales)
    return totalsales

def calcCounty(totalsales):
    countytax = totalsales * 0.02
    return countytax

def calcState(totalsales):
    statetax = totalsales * 0.04
    return statetax

def calcTotal(countytax, statetax):
    total = countytax + statetax
    return total

def printData(total, countytax, statetax):
    print('The county tax is $ ', countytax)
    print('The state tax is $ ', statetax)
    print('The total tax is $ ', total)
main()



