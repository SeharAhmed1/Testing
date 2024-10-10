'''
Created on 02-Oct-2024

@author: Sehar
'''
def func(n):
    if n ==0:
        return 0
    elif n==1:
        return 1 #this is done
    else:
        return (func(n-2)+func(n-1))
    
for x in range(10):
    print(func(x), end = ", ")

(func(10))

def func2(n):
    if n in "abcde":
        return "yeeeey"
    else:
        return "naaayyy"
print(func2("b"))

def missing_number(n):
    
    binary_number=bin(n)[2:]
    #print(binary_number)
    
    if "0" not in binary_number:
        return 0
    count =0
    i=1
    for x in range(len(binary_number)):
        if binary_number[x] == "1":
            while (x+ i) < len(binary_number) and binary_number[x+i]== "0":
                count+=1
                i+=1
            return count
"""print(missing_number((9)))
print(missing_number((529)))"""
print(missing_number((1)))
