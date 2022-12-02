class myclass:
    def myfun(self): #instance method 
        pass
    def display(self,name):
        print("name is ",name)

    @staticmethod
    def vivek():
        print("static method") #static method

mc = myclass()
mc.myfun()
mc.display("vivek")
#calling static method by class name ,no need to create object
myclass.vivek()

#class variables 
class number:
    a,b = 100,50 #class variables

    def add(self):
        print(self.a+self.b) #fetching class variable in methods using self keyword
    def mul(self):
        print(self.a*self.b)
    def div(self):
        print(self.a/self.b)
    def sub(self):
        print(self.a-self.b)

nm = number() #creting object of class 
nm.add() #calling methods using object of class
nm.mul()
nm.sub()
nm.div()