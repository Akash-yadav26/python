#break 
i = 0
while(i<=14):
    i = i+1
    if(i>5 and i<10):
        continue #bypass on this condition
    print(i,end="")
#write a program number is prime or not
a = int(input())
flag = 0 
i = 2
while(i<=a//2):
    if(a%i==0):
        flag =1
    i=i+1
if(flag==0):
    print(i,"is a prime number")
else:
    print(i,"is not a prime ")            
