#operators precedence and associativity

#swaping two number without using third variable
a = int(input("enter a: "))
b = int(input("enter b:"))
# a= a+b# 30+20
# b= a-b# 50-20
# a= a-b#50-30
# print("a =",a,"b= ",b)

# for python only swaping program 
'''akaksh yadav'''
b,a = a,b
print("a .=",)
print("b .=",b)

#write a program ton calculate simple interest
p=float(input("enter the principle amount"))
r= float(input("enter the rate of interest"))
t= float(input("enter the time"))
si = (p*r*t)/100
print("principle amount = ",p)
print("rate of interest = ",r)
print("time =",t)
print("simple intrest = ",si)
#claculate area of circle & diameter
import math 
r=float(input("enetr the radius"))

area = math.pi*r*r
print("area of circle is =",area)
#find number is amstrong or not
#this is not acccurtte way to write amstrong number
a = int(input("enter the number"))
sum = 0 
temp = a
while temp>0 :
  digit = temp%10
  sum += digit*digit*digit
  temp = temp//10

  if  sum == a :
    print(a,"number is amstrong")
else :
  print (a,"is  not a amstrong number")
 
 #multiplying string


  a = "akash yadav"
print(a*6)

#anthor way of print method 
name ="akash"
age = 50

print("Name =%s and age= %d "%(name,age))

#float --> %f