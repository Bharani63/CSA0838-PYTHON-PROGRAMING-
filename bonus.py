n=str(input("enter the grade"))
a=int(input("enter the salary"))
if n=="A":
    c=a*0.05
elif n=="B":
    c=a*0.1
else:
    c=0
print("your salary",a)
print("bonus",c)
print("total salary",a+c)

