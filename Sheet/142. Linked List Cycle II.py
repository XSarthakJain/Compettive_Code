#142. Linked List Cycle II
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
    def detectCycle(self):
        #Approach 1
        slow = fast = self.head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast == None or fast.next == None:
            return None
        slow  = self.head
        while(slow!=fast):
            fast = fast.next
            slow = slow.next
        return slow

        #Approach 2
        headmap = set()
        head =self.head
        while(head):
            if head in headmap:
                return head.data
            else:
                headmap.add(head)
            head = head.next
        return None
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

obj = LinkedList()

obj.push(-5)
obj.push(-2)
obj.push(-5)
obj.push(-9)
obj.push(6)
obj.push(19)
obj.push(-4)
obj.push(7)
obj.push(-7)
obj.push(-1)
obj.head.next.next.next.next.next.next.next.next.next.next = obj.head.next.next.next.next.next.next.next.next.next
#obj.display()
print(obj.detectCycle())
