def Palindrome(s):
    return s == s[::-1]
 
 

s = str(input("enter the string:"))
b=s[::-1]
a = Palindrome(s)
 
if a:
    print("Yes")
    print(s,"reads as",s,"from left to right and from right to left")
else:
    print("No")
    print("From left to right it reads",s," From right to left, it becomes", b," Therefore it is not a palindrome")
