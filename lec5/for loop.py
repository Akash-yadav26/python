# #print number form 1 -10
# i = 1
# while (i<=10):
#     print(i,end="")
#     i+=1
#   i=10

#   while(i>=1):
#     print(i,end="")
#     i-=1    
#write to print factorial of a number
# n = int(input())
# t = 1

# while(n>=1):
#     t*=n
#     n-=1
# print("factorial =",t) # we take print outside loop   so that loop not print every 
#number when it run only this we wnat a single and final result

#check number is perfect
# a= int(input())
# i=1
# sum=0
# while(n>0):
    

#reverse a number
a =int(input())
b=a
rv = 0
d= 1
while(a !=0):
   d = a % 10
   rv = rv*10 + d
   a= a//10 
print("reverse vule",rv)

if( b == rv):
   print(rv,"is palindrom")
else:
   print(rv,"is  not palindrom")     
    
#sir logic
n= int(input("n: "))
n2 =n
rn = n1 = s = 0
while(n>0):
   rn = rn*10+n%10
   n1 = n1+1
   s= s+n%10
   n=n//10
   print("number",n2)
   print("reverse no",rn)
   print("node",n1)
   print("sod",s)
if(n2 == rn):
   print(rn,"is pelendrom")
else:
   print(rn,"is not a palendrom") 
#prime number using break statement 
n = int(input())
i=2
while(i//2):
   if(i<=n//2):
     break
   i=i+1

#loop--> to repeat 
#break --> to get outside the loop
#continue--> to skip the loop
n=int(input("n: "))
i = 0
j=1
a=1
print(i,end="")
print(j,end="")
while(a<=(n-2)):
   k= i+j
   print(k,end="")
   i=j
   j=k
   a=a+1
   