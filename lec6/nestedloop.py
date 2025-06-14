#write program to print 
n=int(input())
i = 1
j=1
while(i<=n):
    j=1
    while(j<=5):
        print(i,end="")
        j=j+1
    print() 
    i=i+1
#print copy pattern
n= int(input("n: "))
i=1
while(i<=n):
    j=1
    while(j<=i):
        print(j,end="")
        j=j+1
    print()
    i=i+1    
#reverse pattern
n= int(input()) 
i=n
while(i>=1):
    j=n
    while(j>=i):
        print(j,end="")
        j=j-1
    print()
    i=i-1    
#pattern 3
n = int(input())
i=1
while(i<=n):
    if(i%2==0):
        j=1
        while(j<=i):
            print("*",end="")
            j=j+1
    else:
        j=1
        while(j<=i):
            print(j,end="")
            j=j+1
    print()                
    i=i+1
#pattern 4
n= int(input("enter n:  "))
i = 1
while(i<=n):
    j=1
    while(j<=i):
        if(j%2==0):
         print("*",end="")
        else:
            print(j,end="")
        j = j+1 
    print()
    i=i+1 
#pattern 5
n = int(input())
i=1
while(i<=n):
    f=1
    while(f<=i):
        if(f%2!=0):
            print("*",end="")
        else:
            print(f,end="")
        f=f+1
    print()
    i=i+1            
    
#pattern 6
n= int(input())
i=k=1
while(i<=n):
    j=1
    while(j<=n):
     print(k,end="")
     k=k+1
     j=j+1
    print()
    i=i+1

#pattern 7
# n = int(input(""))
# i=n 
# while(i>=1):
#     j=i
#     while(j>=1):
#         print(j,end="")
#         j=j-1
#     k=2
#     while(k<=(n-i)+1):
#         print(k,end="")
#         k=k+1
#  print()
#  i=i-1
     