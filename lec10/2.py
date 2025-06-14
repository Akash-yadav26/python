f= open("F:/num1.txt","rt")
f1= open("even.txt","at")
f2=open("odd.txt","at")
for i in f:
    for j in i.split():
        if(int(j)%2==0):
            f1.write(j)
        else:
            f2.write(j)
f1.close()
f2.close()                
# for i in :
#     if(int(i)%2 == 0):
#         f1.write(str(i))
#     else:
#         f2.write(str(i))
# f1.close()
# f2.close()            
f= open("F:/asci.txt","at")
n= int(input("enter 0-127 range"))
for  i in range(-1,n):
    t= str(i)
    f.write(t)
    for j in i.split():
        a=chr(j)
        f.write(a)
        print(a,end=" ")


