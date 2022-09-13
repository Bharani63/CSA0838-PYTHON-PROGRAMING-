def happynum(num):
    c=sum=0
    while(num>0):
        c=num%10
        sum=sum+(c*c)
        num=num//10
    return sum;
a=int(input("enter the number:"))
b=a

while(b!=1 and b!=4):
    b=happynum(b)

if(b==1):
    print(str(a),"is a happy number")

elif(b==4):
    print(str(a),"is not a happy number")
        
