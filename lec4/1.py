
# a= 5
# b=2
# if(a>b):
#     print(b)
#     print(a) #if print comes in if block it considered as outside the if condition only after if else will com not any athor statement

# else:
#     print('c')
#     print('d') 

#  #if- elif-else
#  # nested
# a=int(input())

# if(a>b):
#    if(b>a):
#       print(a)
#    else:
#     print('akash') 
# else:
#    print("akaksh yadav")        

# #write the program  to check number is odd or even
# n=int(input())
# if(n>=0):
#    if(n%2 == 0):
#       print(n,"is a even number")
#    else:
#       print(n,"is a odd number")
# else:
#    print("number is negative number")


# #person is elibgible for voting or not
# name= str(input("Enter your name: "))
# age =int(input("Enter your age"))
# if(age>=18):
#    print(name,"is eligible for voting")
# else:
#   print(name,"is eligible for voting")    
#  #biggest number among three
#  #
# a= int(input("Enter the first num: "))
# b=int(input("Enter the second num: "))
# c= int(input("Enter the third num:"))
# if(a>b & a>c):
#    print(a,"is greatest")
# elif(b>a & b>c):
#    print(b,"is the greatest")
# else:
#    print(c,"is greatest") 
#nested condition

#caculator

# calulater 

print("select operation")
print("1.Add")
print("2.subtract")
print("3.division")
print("4.multiply")

choice = input("Enter choice 1/2/3/4 in order")
if choice in ("1","2","3","4"):
          num1 = float(input('Enter first number: '))
          num2 = float(input('Enter second number: '))
          if(choice == "1"):
            add = num1 + num2
            print(num1,"+",num2,"=",add)
          elif(choice == "2"):
           sub = num1-num2 
           print(num1,"-",num2,"=",sub)
          elif(choice == "3"):
              div = num1/num2
              print(num1,"/",num2,"=",div)
          elif(choice == "4"):
              mul = num1*num2 
              print(num1,"*",num2,"=",mul)
else:
    print("please type in given formate")

#calculate the grade of student
subj= int(input("enter subject 2/3/4/5/6/7 this formate"))
if(subj == 2):
 a = float(input("Enter first subject marks: "))
 b = float(input("Enter second subject marks: "))
 sum = a+b
 per = sum/subj
 print("Total marks :",sum,"percentage :",per,"%")
 if(per >= 90):
    print("Grade: A")
 elif(per<=90 and per>=75):
    print("Grade: B") 
 elif(per<=75 and per>=60):
    print("Grade: C")
 else:
    print("You just passed")

elif(subj == 3):
 a = float(input("Enter first subject marks: "))
 b = float(input("Enter second subject marks: "))
 c= float(input("Enter third subject marks: "))
 sum = a+b+c
 per = sum/subj
 print("Total marks :",sum,"percentage :",per,"%")
 if(per >= 90):
    print("Grade: A")
 elif(per<=90 and per>=75):
    print("Grade: B") 
 elif(per<=75 and per>=60):
    print("Grade: C")
 else:
    print("You just passed")   
elif(subj == 4):
 a = float(input("Enter first subject marks: "))
 b = float(input("Enter second subject marks: "))
 c= float(input("Enter third subject marks: "))
 d= float(input("Enter fourth subject marks: "))
 sum = a+b+c+d
 per = sum/subj
 print("Total marks :",sum,"percentage :",per,"%")
 if(per >= 90):
    print("Grade: A")
 elif(per<=90 and per>=75):
    print("Grade: B") 
 elif(per<=75 and per>=60):
    print("Grade: C")
 else:
    print("You just passed")   
elif(subj == 5):
 a = float(input("Enter first subject marks: "))
 b = float(input("Enter second subject marks: "))
 c= float(input("Enter third subject marks: "))
 d= float(input("Enter fourth subject marks: "))
 e = float(input("Enter fifth subject marks: "))
 sum = a+b+c+d+e
 per = sum/subj
 if(per >= 90):
    print("Grade: A")
 elif(per<=90 and per>=75):
    print("Grade: B") 
 elif(per<=75 and per>=60):
    print("Grade: C")
 else:
    print("You just passed")   
 print("Total marks :",sum,"percentage :",per,"%")
elif(subj == 6):
 a = float(input("Enter first subject marks: "))
 b = float(input("Enter second subject marks: "))
 c= float(input("Enter third subject marks: "))
 d= float(input("Enter fourth subject marks: "))
 e = float(input("Enter fifth subject marks: "))
 f = float(input("Enter sixth subject marks: "))
 sum = a+b+c+d+e+f
 per = sum/subj
 print("Total marks :",sum,"percentage :",per,"%")
 if(per >= 90):
    print("Grade: A")
 elif(per<=90 and per>=75):
    print("Grade: B") 
 elif(per<=75 and per>=60):
    print("Grade: C")
 else:
    print("You just passed")   
elif(subj == 7):
 a = float(input("Enter first subject marks: "))
 b = float(input("Enter second subject marks: "))
 c= float(input("Enter third subject marks: "))
 d= float(input("Enter fourth subject marks: "))
 e = float(input("Enter fifth subject marks: "))
 f = float(input("Enter sixth subject marks: "))
 g=float(input("Enter seventh subject marks: "))
 sum = a+b+c+d+e+f+g
 per = sum/subj
 print("Total marks :",sum,"percentage :",per,"%") 
 if(per >= 90):
    print("Grade: A")
 elif(per<=90 and per>=75):
    print("Grade: B") 
 elif(per<=75 and per>=60):
    print("Grade: C")
 else:
    print("You just passed")   
#year is leap year or not
year = int(input("Enter year in yyy formate"))
if(year%4==0):
    print(year,"is leap year")
elif(year%100==0):
    print(year,"is not leap year") 
#      
    
               
                

        
                 