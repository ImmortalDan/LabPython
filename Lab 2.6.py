# Lab 2.6 Writing a complete program

# This is the main function

def main():
    print('Welcome to the meal calculator program')
    print() # add a blank line

    mealprice = input_meal()
    tip = calc_tip(mealprice)
    tax = calc_tax(mealprice)
    total = calc_total(mealprice, tip, tax)
    print_info(mealprice, tip, tax,total)

# This function will input meal price
def input_meal():
   mealprice = input('Enter the meal price $')
   mealprice = float(mealprice)
   return mealprice

# This function will calculate tip at 20%
def calc_tip(mealprice):
    tip = mealprice * .20
    return tip

# This function will calculate tax at 6%
def calc_tax(mealprice):
    tax = mealprice * .06
    return tax

# This function calculates tip, tax, and the total
def calc_total(mealprice, tip, tax):
    total = mealprice + tip + tax
    return total

# This function will print tip, tax,and the mealprice
def print_info(mealprice, tip, tax, total):
    print('The meal price is $ ', mealprice)
    print('The tip is $', tip)
    print('The tax is $', tax)
    print('The total is $', total)

# calls the main function
main()