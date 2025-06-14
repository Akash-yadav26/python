# # # # # # n=[5,6,7]
# # # # # # for i in range(len(n)):
# # # # # #     n[i] = n[i]*2
# # # # # #     print(n)
# # # # # d = {"a":6}
# # # # # key ="a"
# # # # # if key in d:
# # # # #     print("found")
# # # # # else:
# # # # #     print("nt")    
# # # # def change_value(val):
# # # #     val += [4]
# # # # myList = [1,2,3]
# # # # change_value(myList)
# # # # print(myList)  
# # # c = 5
# # # while(c>0):
# # #     c -= 1
# # # print(c)    
# # a = 8
# # b= 12
# # if a*b < 100:
# #     r = "Product"
# # else:
# #     r= "lamd" 
# # print(r)       
# def count(s):
#     v= "aeiouAEIOU"
#     c= 0
#     for char in s:
#         if char in v:
#             c  += 2
#     return c
# r = count("Hello, World!")
# # print(r)      
# a = -3
# if(a<0 and a%2==0 ):
#     print("land")
# elif(a<0 and a%2!=0): 
#     print("landr")   
# else:
#     print("land4")    

# x = 10 
# x ="ten"
# print(type(x))

# my_set = {10, 20, 30}
# if 10 in my_set:
#     if 20 in my_set:
#         print("both 10 and 20 are present")
#     elif 30 in my_set:
#         print("10 is present and 30 is present")
#     else:
#         print("10 is present but nither 20 nor 30 is present")
# else:
#     print("10 is not present")                


def outer_function(x, y):
    return x + y
add_five_result = outer_function(5, 10)
print(add_five_result)