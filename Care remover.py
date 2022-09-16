def delchar(d,o):
    if(len(o)==1):
        for i in range(len(d)):
            if(o is not d[i]):
                print([d[i]],

                      end="")
            else:
                continue


a=str(input("enter the string:"))
b=str(input("enter the character you want to delete on the setence:"))
print(delchar(a,b))
        
