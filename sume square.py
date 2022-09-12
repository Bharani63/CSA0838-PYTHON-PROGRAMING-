l=[]
a=int(input("Enter the list limit:"))
for i in range(0,a):
    b=int(input("Enter element:"))
    l.append(b)
print(l)
def squaresum(a):
    odd=0
    even=0
    for i in a:
        if(i%2==0):
            even=even+i**2
        else:
            odd=odd+i**2
    a=[odd,even]
    return a
print(squaresum(l))
