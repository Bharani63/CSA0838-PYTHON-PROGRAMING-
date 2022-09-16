def combination(k, i=0):
    if i== len(k):
        print("".join(k))
    for j in range(i, len(k)):
        flame=[c for c in k]
        flame[i], flame[j] = flame[j], flame[i]
   	 

        combination(flame, i + 1)

a=str(input("enter the number:"))
print(combination(a))



