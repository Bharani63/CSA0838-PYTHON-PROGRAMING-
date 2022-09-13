a=int(input("entr the count of fresh loaves you purchased:"))
b=int(input("entr the count of old loaves you purchased:"))
if(a>0)and(b>0):
    dis=185*0.6
    c=a*185
    d=b*dis
    total=c+d
    print("regular price=185.00")
    print("amount of new loaves=",'%.2f'%c)
    print("amount of old loaves=",'%.2f'%d)
    print("total amount=",'%.2f'%total)

    
else:
    print("invalid input")
    pass
