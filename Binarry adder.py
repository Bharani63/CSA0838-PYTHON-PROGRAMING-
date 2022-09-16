print("Enter First Binary Number: ")
x = int(input())
print("Enter Second Binary Number: ")
y = int(input())

x = str(x)
y = str(y)
z= int(x, 2) + int(y, 2)
c = bin(z)

print("Result = " , c)

