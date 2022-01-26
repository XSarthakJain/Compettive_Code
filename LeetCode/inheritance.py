class A:
    def sum(self,a,b):
        print("A",a+b)

class B:
    def sum(self,a,b):
     print("B",a+b)

class C(B,A):
    def __init__(self):
        pass

obj1 = C()
obj1.sum(5,5)
