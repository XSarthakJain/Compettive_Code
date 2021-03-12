#class Creation
class Test:
    def __init__(self):
        self.ind = 0
    def fun(self):
        print("Hello")
    def get_ind(self):
        print(self.ind)
    def set_ind(self,val):
        self.ind = val

#driver Code
obj = Test()
obj.fun()
obj.get_ind()
obj.set_ind(5)
obj.get_ind()

    
