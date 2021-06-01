class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    def Display(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
def Merge(list1,list2):
    temp1 = list1.head
    temp2 = list2.head
    thirdLinkedList = Node(-1)
    thirdNode = thirdLinkedList
    
    while(True):
        if temp1 is None:
            thirdNode.next = temp2
            break
        if temp2 is None:
            thirdNode.next = temp1
            break
        
        if(temp1.data<temp2.data):
            thirdNode.next = temp1
            temp1 = temp1.next
        else:
            thirdNode.next = temp2
            temp2 = temp2.next
        thirdNode = thirdNode.next
    return thirdLinkedList.next
            
if __name__ == "__main__":
    #First LinkedList
    obj = LinkedList()
    obj.head = Node(5)
    obj2 = Node(10)
    obj3 = Node(15)
    obj4 = Node(20)
    obj5 = Node(31)

    obj.head.next = obj2
    obj2.next = obj3
    obj3.next = obj4
    obj4.next = obj5

    #obj.Display()

    #Second LinkedList
    secObj = LinkedList()
    secObj.head = Node(2)
    secObj2 = Node(6)
    secObj3 = Node(11)
    secObj4 = Node(16)
    secObj5 = Node(28)

    secObj.head.next = secObj2
    secObj2.next = secObj3
    secObj3.next = secObj4
    secObj4.next = secObj5

    #secObj.Display()

    #Merge
    
    thirdLinkedList = LinkedList()
    thirdLinkedList.head = Merge(obj,secObj)
    thirdLinkedList.Display()
    

    
