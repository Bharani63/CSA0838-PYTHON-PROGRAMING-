def profit(pri,j):
    profit=[0]*j
    max_pri=pri[j-1]
    for i in range(j-2,0,-1):
        if(pri[i])>max_pri:
            max_pri=price[i]
        profit[i]=max(profit[i+1],max_pri-price[i])

    min_price=price[0]
    for j in range(1,j):
        if price[j]<min_price:
            min_price=price[j]
        profit[j]=max(profit[j-1],profit[j]+(price[j]-min_price))
    ans=profit[j-1]
    return ans


price=[]
a=int(input("enter the limit:"))
for i in range(0,a):
    b=int(input("enter the buy and sell price:"))
    price.append(b)
print(price)
print("max_profit is:",profit(price,len(price)))
