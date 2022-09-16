n=str(input("enter the string:"))
k=int(input("enter the occurance:"))

m=n
n.split()
m.split()
cnt=0
for i in range(len(n)):
    for j in range(len(m)):
        if n[i]==m[i]:
            cnt=1
        elif n[i]!=m[i]:
            cnt+=1
print(cnt)
            
