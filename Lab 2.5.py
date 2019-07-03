# This program demonstrates how to use variables and functions

# This program uses functions and variables

# The main function

def main():
    print('Welcome to the tip culculator program')
    print() # prints a blank line

    name = inputName()
    age = inputAge()

    print('Hello', name)

    print('Your age is ', age)



# This function inputs data
def inputName():
    name = input('Enter your name: ')
    return name
# This function inputs age
def inputAge():
    age = input('Enter your age: ')
    return age
# calls main function
main()

