def add(a,b):
    print(a + b)

def subtraction(a,b):
    print(a - b)

def mul(a,b):
    print(a * b)

def div(a,b):
    print(a / b)

print("Hello")
a = int(input("Enter your first Number - "))
b = int(input("Enter your first Number - "))

x = int(input('''
              If you want to add then press 1 ,
              if you want to Subtrack then press 2 
              if you want to Multiply then press 3 
              if you want to Divide then press 4  '''))

if x == 1:
    add(a,b)
elif x == 2:
    subtraction(a,b)
elif x == 3:
    mul(a,b)
elif x == 4:
    div(a,b)
else:
    print("Invalid Input")
    exit