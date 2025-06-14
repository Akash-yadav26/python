def myfun(a,b):
    return (a+b)
c= myfun(10,30)
print(c)
#types of function
#without parameter
def abc():
    print("hello")
abc()
#with parameter
def abc():
    print("bye")
abc()  
#

def add():
  a= 10
  b=20
  c=a+b
  print(c)
def div(a,b):
    return(a//b)
add()
print("sum",add())
a = int(input("enter a: "))
b = int(input('enter b: '))
d=div(a,b)
print("divsion =",d)

#------------>
def abc():
    print("abc is called")
def xyz():
    abc()
    print("xyz also called")
abc()
xyz()  
#without return function only print none when they are in print function
#beacuse they treated as string

#higher order function
def x():
    print('hello world')
def y(j):
    j()
    print("abc is aphabet")
y(x)   
#variable length argument
def abc(a,*b):
    print(a,end="")
    for i in b:
 
       print(i,end="")
abc(10)
abc(10,20,30)
abc(5,10,15,20,25)



print()
def ffg(a,b):
    print((a+b))
ffg(34,56)  



 


