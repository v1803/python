#Dictionary is a collection of key and value pairs
myDict ={
    "fast":"is a quick learner",
    "vivek":"good boy",
    "marks":[3,33,333],
    "anotherdict":{"verion":"developer"},
    1:2
}
print(myDict["fast"])
print(myDict["marks"])
myDict['marks'] = [45,78]
print(myDict['marks'])
print(myDict['anotherdict']['verion'])

#methods
print(myDict.keys())
print(myDict.values())
print(myDict.items())
uDict ={
    "ravi":"tester"  #update
}
myDict.update(uDict)
print(myDict)
print(myDict.get('vivek'))