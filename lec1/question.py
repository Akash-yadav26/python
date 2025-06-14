a = int(input("enetr a number"))

if a % 2 == 0: #after colon space is require or it shows the error
 print("even")
else :
 print("odd")

 #factorial of number only for value 6
 # to show how loop works

 n = int(input("enter a  number :"))
 f= 1
 if n>=1 :
  f = f*n
 n= n-1
 if n>=1:
  f= f*n
 n= n-1
 if n>=1:
  f = f*n
  n= n-1
  if n>=1:
    f= f*n
    n= n-1
    if n>=1:
      f= f*n
      n= n-1
      if n>=1:
       f= f*n
       n=n-1
       if n>=1:
        f=f*n
print(" factorial =",f)

#find the factorial of number 
n = int(input("enter the number"))
f=1
for i in range(1,n-1):
 f *= i
 print("factorial = ",f)

#find the average of three number
a = float(input("enter first number"))
b= float(input("enter second number"))
c = float(input("enter third number"))
avrg = (a+b+c)/3
print("average of the numbers is = ",avrg)
#swap a number using thrid varialble
a = int(input("enter a:"))
b= int(input("enter b:"))
d = a
a=b
b= d
print("value of swap :")
print("value of a",a)
print("value of b",b)
#find the area and parimeter of the circle
import math
r= float(input("enter radius of circle"))
area = math.pi*r**2
parameter = 2*math.pi*r
print("parameter is =",parameter)
print("area of circle = ",area)

#check if a number is divide by 7 or not
a = int(input("enter the number"))
if a%7 == 0 :
 print(a," is divisible by 7")
else:
 print(a,"is not divsible by 7")
 #among the three number : a,b and c find the greater number
a = int(input("enter a :"))
b = int(input("enter b:"))
c = int(input(" enter c :"))
if a>=b and a>=c :
 print(a," is greater")
elif b>= a and b>=c :
 print (b,"is greater")
else:
 print(c,"is greater")
 # to check number is amstrong number or not
 a = int(input("enter the number"))
 
 


