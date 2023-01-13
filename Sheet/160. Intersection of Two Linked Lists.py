#160. Intersection of Two Linked Lists
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    def display(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def getIntersectionNode(headA,headB):
    if headA is None or headB is None:
        print("None Executed = ")
        return None
    tempA = headA
    tempB = headB
    while(tempA!=tempB):
        
        tempA = headB if tempA==None else tempA.next
        tempB = headA if tempB==None else tempB.next
    return tempA.data

    '''
    tempA = headA
    tempB = headB
    templen = 0
    lenA = 0
    lenB = 0
    #print("Pointes = ",headA.data,headB.data)
    while(tempA is not None and tempB is not None):
        templen+=1
        #print("Pointes = ",tempA.data,tempB.data,templen)
        tempA = tempA.next
        tempB = tempB.next
    #print("Pointes = ", templen)
    
    lenA = lenB = templen
    while(tempA):
        lenA+=1
        tempA = tempA.next
        headA = headA.next
    while(tempB):
        lenB+=1
        tempB = tempB.next
        headB = headB.next
    #print("length = ",lenA,lenB,headA.data,headB.data)
    
    #print(lenA,lenB,headA.data)
    
    while(headA is not None and headB is not None):
        #print(headA.data,headB.data)
        if headA == headB:
            return headA.data
        headA = headA.next
        headB = headB.next
    return None
    '''
obj = LinkedList()
obj.push(5)
obj.push(10)

obj.display()
obj1 = LinkedList()
obj1.push(1)
obj1.push(2)
obj1.push(3)
obj1.push(4)
obj1.push(5)
obj1.push(6)
print("Linked List 2")
obj.head.next.next = obj1.head.next.next.next
obj.display()
print("Intersection = ")
print(getIntersectionNode(obj.head,obj1.head))
