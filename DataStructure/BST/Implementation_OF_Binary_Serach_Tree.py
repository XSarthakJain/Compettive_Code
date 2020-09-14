#Binary Search Tree 12:16
class BST:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def addChild(self,data):
        
        if self.data==data:
            return
        
        if data>int(self.data):
            if self.right:
                self.right.addChild(data)
            else:
                self.right=BST(data)
        else:
            if self.left:
                self.left.addChild(data)
            else:
                self.left=BST(data)
    def Preorder(self):
        print(self.data)
        if self.left:
            self.left.Preorder()
        if self.right:
            self.right.Preorder()

def Build(data1):
    root=BST(data1[0])

    for i in range(1,len(data1)):
        root.addChild(data1[i])
    return root

if __name__=="__main__":

    l1=[5,10,15,25,2]
    n1=Build(l1)
    n1.Preorder()
    
            
