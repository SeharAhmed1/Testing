'''
Created on 10-Oct-2024

@author: Sehar
'''
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