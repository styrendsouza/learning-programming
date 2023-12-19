

userInput = input("Please enter a number ")

intUserInput = int(userInput)
floatUserInput = float(userInput)

print(userInput)
print(intUserInput)
print(floatUserInput)


if intUserInput % 2 == 0:
    print("It's an Even Number")
else:
    print("It's an Odd Number")
    
if intUserInput == 0:
    print("Your Number is 0")
elif intUserInput > 0:
    print("positive") 
else:
    print("Negitive")

newUserInput = intUserInput + 2
print(newUserInput)

areaOfSquare = intUserInput ** 2
print("the area of a Square is " + str(areaOfSquare))

a = input("What is your name? ")
b = input(" What is your surname? ")

A = a
a = b
b = A

print(b + " " + a)
