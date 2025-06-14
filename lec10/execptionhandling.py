a = int(input())
b = int(input())
try:
    quo = a/b
    print("Quotient",a)
except ZeroDivisionError:
    print("Denominator cannot be zero") 
except ValueError:
    print("please enter numeric value")       
finally:
    print("finally ecexuted")
#in upper code the value error not defined inside the try  block that why it not caught the error

try:
    a = int(input())
    b = int(input())
    quo = a/b
    print("Quotient",a)
except ZeroDivisionError:
    print("Denominator cannot be zero") 
except ValueError:
    print("please enter numeric value")       
finally:
    print("finally ecexuted")

#raise --> by raise we can chnage nature of massgae of error
x= "hello"
if not type(x) is int:
    raise ValueError("only integer value allowed")
    