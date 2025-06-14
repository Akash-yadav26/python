#string slicing
# stirng store in the form of array 
#start with 0 and -1 at end se start --> write in note book
#[start index: end index: step size] for slicing
# default vaalue
#  [0:length():1 or any number0]
#  index called length
#list [34,45,5666,6,6,67]





s= "hello niet"
print(s[:6:2])
t="akash yadav"
print(t[:4:3])
print(t[::-1])

h = {}
print(type(h))
tupple = (23,2324,44)
print(tupple[:3:])
print(type(tupple))
t= (45,45,45,(34,34,56),(34,35,567),(34,45,56,56),(4,345,45,56,56,),(34,45,56,56))
print(t[3][0] ,t[5])

s= ()
r=[]
t= {}
b= set()
set = {34,34,56}
print(type(b))
print(type(r))


set = {34,56,78,78,78,78,78,78,78,78,78} # repetation not allowed in set
print(set)

s={"aak":45,"rrh":45}
print(s['rrh'])
#to  make change in dict
s['rrh'] = 60



print(s)
#to print only keys
for key in s.keys():
    print(key)
a = "20"