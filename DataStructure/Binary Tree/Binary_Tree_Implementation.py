#Binary Tree
class Node:
    def __init__(self,data):
        self.data=None
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
    def Insert(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            if self.data<data:
                Insert(self.right,data)
            else:
                Insert(self.left,data)
        

t1=tree()
t1.Insert(10)
t1.Insert(20)
