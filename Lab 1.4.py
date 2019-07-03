# Dan Munene
# July 3rd
# This program contains the code for lab 1 tests

studentName = input('Enter student name.')
degreeName = input('Enter degree name')
creditsDegree = int(input('Enter the number of credits required for the degree. '))
creditsTaken = int(input('Enter the number of credits taken so far. '))

creditsLeft = creditsDegree - creditsTaken

print("The student's name is", studentName)
print("The degree name is", degreeName)
print("There are", creditsLeft, "credits left until graduation")