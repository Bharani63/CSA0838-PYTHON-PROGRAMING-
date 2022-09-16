from math import factorial as fact
a=int(input("enter the number of rows:"))
b=int(input("enter the row number:"))
for i in range(a):
    for j in range(a-i+1):
        print(end=" ")
    for j in range(i+1):
        print(fact(i)//(fact(j)*fact(i-j)),end=" ")
    print()

for i in range(0,b+1):
    c=2**i
print("the sum:",c)
