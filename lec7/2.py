#write a program to calculate factorial using recursion

def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
s=int(input())
print("factorial = ",fact(s))    
#write a program to calculate factorial usinng addition
def rsum(a,b):
    if(b==1):
        return a
    else:
        return a+rsum(a,b-1)
print("multiplication = ",rsum(3,4)) 
#

