#list methods

lst = [1,4,5,3,2]
lst.sort() #it sorts the list
print(lst)
lst.reverse() #it reverse the list
print(lst)
lst.append(9) # it add the element in last
print(lst)
lst.insert(2,44) #insert the element of given index
print(lst)
lst.pop(6) #it remove the index element
lst.remove(44)  #it remove the element
print(lst)

#program 1 --> input 7 fruits and print in list

f1 = input("Enter Fruit number 1")
f2 = input("Enter Fruit number 2")
f3 = input("Enter Fruit number 3")
f4 = input("Enter Fruit number 4")
f5 = input("Enter Fruit number 5")
f6 = input("Enter Fruit number 6")
f7 = input("Enter Fruit number 7")
fruits =[f1,f2,f3,f4,f5,f6,f7]
print(fruits)

#program 2 ---> studnet mark and sort in list

m1 = int(input("Enter student number 1 : "))
m2 = int(input("Enter student number 2 : "))
m3 = int(input("Enter student number 3 : "))
m4 = int(input("Enter student number 4 : "))
m5 = int(input("Enter student number 5 : "))
m6 = int(input("Enter student number 6 : "))
student_mark =[m1,m2,m3,m4,m5,m6]
student_mark.sort()
print(student_mark)

#program 3 --> sum of list
a = [23,4,5,6]
print(a[0]+a[1]+a[2]+a[3])
print(sum(a))