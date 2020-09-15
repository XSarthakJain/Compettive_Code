#Binary Search Tree 12:16
class BST:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def addChild(self,data):
        
        if self.data==data:
            return
        
        if data>self.data:
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

    def Search(self,data):
        #print("self.data",self.data,data)
        if self.data==data:
            print("True")
            return True

        if data<self.data:
            if self.left:
                self.left.Search(data)
            else:
                print("False")
                return False
        else:
            if self.right:
                self.right.Search(data)
            else:
                print("False")
                return False
    def MinValueTree(self):
        current=self
        
        while(current.left is not None):
            current=current.left
        return current

    def Deletion(root,key):
        print("yghyuhjguyg",root.data)
        if root is None:
            return root
        
        elif key>root.data:
            root.right=root.right.Deletion(root.right,key)
        elif key<root.data:
            root.left=root.left.Deletion(root.left,key)
        else:
            if root.left is None:
                temp=root.right
                root=None
                return temp
            elif root.right is None:
                temp=root.left
                root=None
                return temp
            else:
                temp=root.right.MinValueTree()
                print("temp.data",temp.data)
                root.data=temp.data
                root.right=root.right.Deletion(temp.data)

        return root
            
            
            
        

def Build(data1):
    root=BST(data1[0])

    for i in range(1,len(data1)):
        root.addChild(data1[i])
    return root

if __name__=="__main__":

    l1=[5,10,15,25,2]
    n1=Build(l1)
    n1.Preorder()
    n1.Search(2)

    n1=n1.Deletion(5)
    n1.Preorder()
            
