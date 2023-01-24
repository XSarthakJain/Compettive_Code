#Flattening a Linked List
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,data,bottomLL=None):
        newNode = Node(data,bottomLL)
        newNode.next = self.head
        self.head = newNode
    def display(self):
        temp = self.head
        while(temp):
            print(temp.data)
            #temp1 = temp.bottom
            temp = temp.next
    def Flattening(self):
        temp = self.head
        while(temp):
            if temp.bottom:
                nextNode = temp.next
                temp.next = temp.bottom
                while(temp.next):
                    temp = temp.next
                temp.next = nextNode
            temp = temp.next
    def midium(self,head):
        slow,fast = head,head.next
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        return slow
    # Merge Sort 
    def merge(self,left,right):
        if left is None:
            return right
        if right is None:
            return left
        result = temp = Node(1,None)
        while(left and right):
            if left.data<=right.data:
                result.next = left
                left = left.next
            else:
                result.next = right
                right = right.next
            result = result.next
        if left:
            result.next = left
        if right:
            result.next = right
        return temp.next
    def mergesort(self,head):
        if head is None or head.next is None:
            return head
        mid = self.midium(head)
        left = head
        right = mid.next
        mid.next = None
        left = self.mergesort(left)
        right = self.mergesort(right)
        return self.merge(left,right)
class Node:
    def __init__(self,data,childll):
        self.data = data
        self.next = None
        self.bottom  = childll
obj = LinkedList()
obj1 = LinkedList()
obj1.push(45)
obj1.push(40)
obj1.push(35)
obj.push(28,obj1.head)
obj2 = LinkedList()
obj2.push(50)
obj2.push(22)
obj.push(19,obj2.head)
obj3 = LinkedList()
obj3.push(20)
obj.push(10,obj3.head)
obj4 = LinkedList()
obj4.push(10)
obj4.push(8)
obj4.push(7)
obj.push(5,obj4.head)
#obj.display()
print("Flattening = ")
obj.Flattening()
#obj.display()
obj.head = obj.mergesort(obj.head)
obj.display()
        
