# i = 1
# while i <= 100:
#     print(i, end=" ")
#     i += 1

a= int(input("enter b :"))
b= int(input("enter a:"))
z = a-b
c= a+b
t = a*b
y= a/b
print( "sum",c)
print("product",t)
print("divide",y)
print("difference is",z)

n = int(input("enter calcius"))

h = n*9/5+ 32
print(h,"F")

import math 

a = float(input("enter a:"))
b= float(input("enetr b: "))
c= float(input("enter c :"))

disc =(b**2)-(4*a*c)
x1 = (-b-math.sqrt(disc)/2*a)
x2 = (-b+math.sqrt(disc)/2*a)
print(x2,x1)

if disc>0 :
    print(" 2 real solution  ")
elif disc==0 :
 print("1 real solution")  
else :
   print("2 imaginary solution") 
#sqrt used for square root
# x1 = (-b-math.sqrt(disc)/2*a)
# x2 = (-b+math.sqrt(disc)/2*a)
# print(x2,x1)


#cubic roots
# import math
# a = float(input("enetr a:"))
# b= float (input("enter b:"))
# c= float(input("enter c:"))
# disc = (b**2) - (4*a*c)
# x1= -b-math.sqrt(disc/2*a)
# x2 = -b+math.sqrt(disc/2*a)
# print("x1 = ",x1)


