#Method Overloading
'''
Method Overloading is an example of Compile time polymorphism. In this, more than one method of the same class shares the same method name having different signatures. Method overloading is used to add more to the behavior of methods and there is no need of more than one class for method overloading.
Note: Python does not support method overloading. We may overload the methods but can only use the latest defined method.
'''
class functionality:
    def __init__(self):
        self.name = ""
        self.age = 0
    def addDetails(self,name):
        self.name = name
    def addDetails(self,age):
        self.age = age
    def display(self):
        print("Details",self.name,self.age)
obj = functionality()
obj.addDetails("XYZ")
obj.addDetails(5)
obj.display()
