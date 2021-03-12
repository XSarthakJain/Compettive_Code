#Inheritance
class parent:
    def __init__(self):
        self.name = ""
    def parent_method(self):
        print("Parent Method call")
        
class child(parent):
    def child_method(self):
        print("Child Method call")

obj = child()
obj.child_method()
obj.parent_method()
