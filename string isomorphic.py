def isisomarphic(str1,str2):
    if len(str1)!=len(str2):
        return False
    else:
        m1,m2={},{}
        for i in range (len(str1)):
            c1,c2=str1[i],str2[i]
            if c1 not in m1:
                m1[c1]=c2
            if c2 not in m2:
                m2[c2]=c1
            if m1[c1]!=c2 or m2[c2]!=c1:
                return False
        return True
str1=str(input("Enter your string1:"))
str2=str(input("Enter your string2:"))
print(isisomarphic(str1,str2))
