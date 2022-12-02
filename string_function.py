paragraph = "python is a popular programming language. It was created by Guido van Rossum, and released in 1991"
#string functions
print(len(paragraph))
print(paragraph.endswith("1991"))
print(paragraph.count("p"))
print(paragraph.capitalize()) #it will convert only first word in capital letter
print(paragraph.find("Rosd")) #it will return first occurance index value otherwise -1
print(paragraph.replace("python","java")) #it will replace all occurances the string with new string 

#programs 1

name = input("Enter your name: ")
print("Good Morning, "+name)

#program 2

letter = ''' Dear <|NAME|>,
You are selected !
Date:<|DATE|>            
'''
name = input("Enter your name: ")
date = input("Enter date")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)

#program 3

st = "this is a double space string            in program "
print(st)
print(st.find("  ")) #find double space index

str = "this is a double space string    in program "
print(str.replace("  "," ")) #replace double space with single space

