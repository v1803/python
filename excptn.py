#before handling exception

# print("Program is started")
# print(10/0)  #ZeroDivisionError: division by zero
# print("program is completed")


#before handling exception

from argparse import ONE_OR_MORE


print("Program is started")
try:
    print(10/0)
except ZeroDivisionError:
    print("Entered into except block - handled exception")

print("program is completed")

#we can raise our own exception using 'raise' keyword

def enterage(age):
    if age<0:
        raise ValueError("only positive integers are allowed")
    if age%2==0:
        print("age is even")
    else:
        print("age id odd")

# num=-1
# enterage(num)

try:
    num = -1
    enterage(num)
except ValueError:
    print("only positive integers are allowed")
except:
    print("Something is wrong")


#exception handled by object
try:
    number = one
    print(number)
except NameError as ex:
    print("exception is ", ex)