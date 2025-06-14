#same patteern using python inbulidn function
n= int(input())
for i in range (1,(n//2+1)):
    if(n%i==0):
        print(n,"is a prime number")
        break
    else:
        print(n,"is not a prime number")
#reverse number using slicing
n = input("enter a number")
rn = n[::-1]
n= int(rn)
print("reverse number",rn) 
#find numbe roff vowels and consonent
s= input("enter latter")
v=c=0
l=["a","e","i","o","u","A","E","I","O","U"]
for i in s:
    if i in l:
        v=v+1
    else:
        c=c+1
print("no of vowels: ",v)
print("no of consonent: ",c)            
#to print all prime number from 1 to 100
a =int(input())
for i in range(2,101):
 for j in range(2,(i//2+1)):
  if(i%j==0):
      break
  else:
      print(i)