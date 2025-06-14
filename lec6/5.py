#reverse the number

n = int(input())
i =1
while(i<=n):
    j=1
    while(j<=n):
        print(i,end="")
        j=j+1
    print()
    i=i+1  
#pattern2
n = int(input())
i=1
while(i<=n):
    f=1
    while(f<=i):
        print(f,end="")
        f=f+1
    print()
    i=i+1
#pattern3
n =  int(input())
i = n
while(i>=1):
    j=n
    while(j>=i):
        print(j,end="")
        j=j-1
    print()
    i=i-1         
#pattern4
n=int(input())
i=1
while(i<=n):
    if(i%2==0):
        j=1
        while(j <= i):
          print("*",end="")
          j=j+1
    else:
           j=1
           while(j<=i):
            print(j,end="")
            j=j+1

    print()
    i=i+1    
#pattern5
n=int(input())
i = 1
while(i<=n):
    j=1
    while(j<=i):
        if(j%2==0):
            print("*",end="")
        else:
            print(j,end="")
        j=j+1
    print() 
    i+=1           
#pattern6
n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=i):
        if(j%2!=0):
            print("*",end="")
        else:
            print(j,end="")
        j=j+1
    print()
    i=i+1 
#pattern7
#pascal triangle
row = int(input("enter a number of rows"))
k=1
for i in range(1,row+1):
    for a in range(1,(row-i)+1):
        print(" ",end="")
    for j in range (0,i):
        if j==0 or i==0:
            k=1
        else:
            k=k*(i-j)//j
        print(k,end=" ")
    print()   


#pascal triangle method-->2


