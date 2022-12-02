#set is not store repeatative element
a = {1,2,3,4}
print(type(a))
print(a)
#it will be a empty dictionary not a set
b = {}
print(type(b))
#creating a empty set
c = set()
print(type(c))
c.add(5)
print(c)
# c.add([2,4,5]) #cant add list in set
# c.add({"vivek":"developer"}) #cant add dictionary in set
print(len(a)) #length of set
a.remove(3) #remove 3 from set a
print(len(a))


#program 1
mD = {
    "pankha":"fan",
    "dabba":"box",
    "ghadi":"watch"
}
print("my options are : ", mD.keys())
a = input("Enter the hindi word\n")
print("the meaning of your word is :",mD[a])