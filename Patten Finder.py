import re
F = input("Enter the first string:")
p = input("Enter the second string:")
p = r"{}".format(F)
p = re.compile(F)
if p.fullmatch(F):
    print("True")
else:
    print("False")
