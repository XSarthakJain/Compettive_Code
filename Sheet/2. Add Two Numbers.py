#2. Add Two Numbers
class LinkedList:
    def __init__(self):
        self.head  = None
    def push(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    def display(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
def addition(l1,l2):
    carry = 0
    head1 = l1
    pointer = l1
    head2 = l2

    while(head1 is not None and head2 is not None):
        temp = head1.data + head2.data + carry
        pointer = head1
        head1.data = temp%10
        carry = temp//10
        head1 = head1.next
        head2 = head2.next
    while(head1):
        temp = head1.data + carry
        head1.data = temp%10
        carry = temp//10
        pointer = head1
        head1 = head1.next
    if head2:
        pointer.next = head2
    while(head2):
        temp = head2.data + carry
        head2.data = temp%10
        carry = temp//10
        pointer = head2
        head2 = head2.next
    if carry!=0:
        pointer.next = Node(carry)
    return l1
            
            
            
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
obj = LinkedList()
obj.push(5)
obj.push(10)
obj2 = LinkedList()
obj2.push(15)
obj2.push(20)
obj2.push(25)
obj5 = LinkedList()
obj5.head = addition(obj.head,obj2.head)
obj5.display()

        
