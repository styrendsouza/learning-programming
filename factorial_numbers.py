userInput = int(input(" Enter A Number"))

x = 1
for i in range(1,userInput + 1):
    x = x * i

print(x)

# fibonacci sequence
d = int(input("enter a number"))
a = 0
b = 1

print(a)
print(b)

for i in range(2,d):
    c = a + b
    a = b
    b = c 
    print (c)