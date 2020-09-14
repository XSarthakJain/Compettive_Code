#Tree Implementation
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.child=[]
        self.parent=None

    def addChild(self,data):
        data.parent=self
        self.child.append(data)
    def PrintData(self):
        print(self.data)
        if self.child:
            for i in self.child:  
                i.PrintData()
                

t1=TreeNode(5)

t2=TreeNode(10)
t1.addChild(t2)
t3=TreeNode(11)
t1.addChild(t3)
t4=TreeNode(12)
t1.addChild(t4)
t5=TreeNode(13)
t2.addChild(t5)
        
t1.PrintData()
