def countstr(n,start):
    if(n==0):
        return 1
    count=0
    for i in range(start,5):
        count+=countstr(n-1,i)
    return count
def vowel(n):
    
    return countstr(n,0)
    

f=int(input("enter the input:"))
print(vowel(f))
