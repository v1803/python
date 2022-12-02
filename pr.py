# a=45
# b=15
# print(a+b)
# print(a%b)
# print(a>b)
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print((a+b)//2)
# a=5
# print(type(a))

# import calendar
# print(calendar.month(2050,12))
 
import calendar 
yy = int(input("Enter Year"))
mm = int(input("Enter Month"))
print(calendar.month(yy,mm))

# a,b = 23,12 #ternary operator
# max = a if a>b else b
# print(max)

#swap
a, b = 32, 45
b,a=a,b
print(a,b)