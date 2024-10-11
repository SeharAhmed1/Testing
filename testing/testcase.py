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


print("now this")
print("Aniya is being very annoying")
print("now she is not annoying")

