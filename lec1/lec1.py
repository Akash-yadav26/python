a = 5
b = 7
print(a+b)

#to print ecide number is even is odd


#check data types 
#10---> int
#10.3--> float/double
#10+20j --> complex

a= 10.2
print(type(a))
b= 10+7j #--> only for j or i is not use
print(type(b))
s="hello"
print(type(s))
#to check number is perfect number or not 

Input_Number = 6
Sum = 0
for i in range(1, Input_Number):
    if(Input_Number % i == 0):
        Sum = Sum + i
if (Sum == Input_Number):
    print("Number is a Perfect Number")
else:
    print("Number is not a Perfect Number")

a= input("enter :b")#10
t= input("enter : a")#20
d = a+t
print("sum = ",d)#1020

#behave as string not number

#type casting
#a= "10"# for string
#b= int(input(10)) # for const value

r= int(input("enter a:"))
f = int(input("eneter b:"))
v = r+f
print('sum',v)




    

