import collections
 
 

def getMinimumOperations(first, second):
    
    count = 0
 
    
 
    
    a = len(first) - 1
    b = i
 
    while b >= 0:
        
        while a >= 0 and first[a] != second[b]:
            a = a - 1
            count = count + 1
 
        a = a - 1
        b = b - 1
 
    
    return count
 
 

def isTransformable(first, second):
    
    if len(first) != len(second):
        return False
 

    
    return collections.Counter(first) == collections.Counter(second)
 
 
if __name__ == '__main__':
 
    first = str(input("enter the word1:"))
    second = str(input("enter the word2:"))
 
    if isTransformable(list(first), list(second)):
        print('The minimum operations required to convert the String', first,
              'to string', second, 'are', getMinimumOperations(first, second))
    else:
        print('The string cannot be transformed')
  
