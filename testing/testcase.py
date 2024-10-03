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
