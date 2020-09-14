#Binary Tree
class tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def addChild(self,data):
        
        if self.left is  None:
            self.left=data
        else:
            self.right=data

    def Inorder(self):
        #left->Node->right
        if self.left:
            self.left.Inorder()
        print(self.data)
        if self.right:
            self.right.Inorder()

    def Preorder(self):
        print(self.data)
        if self.left:
            self.left.Preorder()
        if self.right:
            self.right.Preorder()
    def Postorder(self):
        if self.left:
            self.left.Postorder()
        if self.right:
            self.right.Postorder()
        print(self.data)
    
        

t1=tree(5)
t2=tree(10)
t3=tree(15)
t4=tree(20)
t5=tree(25)
t6=tree(30)
t1.addChild(t2)
t1.addChild(t3)
t2.addChild(t4)
t2.addChild(t5)
t4.addChild(t6)
print("Inorder")
t1.Inorder()
print("preorder")
t1.Preorder()
print("Postorder")
t1.Postorder()
