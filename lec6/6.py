#for loop
n = int(input())
for i in range(1,n):
    for j in range(1,i+1):
        print("*",end="")
    print() #newline hacker

#for
from math import factorial
r = int(input("how many rows"))
for i in range(r):
    print(" "*(r-i+1),end="")
    for j in range(i+1):
        print(factorial(i) // (factorial(i-j)*factorial(j)),end=" ")
    print()    
