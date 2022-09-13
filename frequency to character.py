def ftoc(o):
    frequency = [0] * 26
    n = len(o)
    for i in range(n):
        frequency[ord(o[i]) - ord('a')] += 1
    for i in range(n):
        add = frequency[ord(o[i]) - ord('a')] % 26
        if(ord(o[i])+add<=ord('z')):
            o[i] = chr(ord(o[i])+add)
        else:
            add = (ord(o[i]) + add) - (ord('z'))
            o[i] = chr(ord('a') + add - 1)
    print("".join(o))
if __name__ == '__main__':
    str = str(input("enter the string:"))
    ftoc([i for i in str])




