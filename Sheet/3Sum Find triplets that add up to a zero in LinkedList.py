#3 Sum : Find triplets that add up to a zero in LinkedList
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
    def tripleSum(self):
        temp = self.head
        result = []
        while(temp.next.next):
            temp1 = temp.next
            while(temp1.next):
                temp2 = temp1.next
                while(temp2):
                    if (temp.data + temp1.data + temp2.data) == 0:
                        tempresult = [temp.data,temp1.data,temp2.data]
                        tempresult.sort()
                        if tempresult not in result:
                            result.append(tempresult)
                    temp2 = temp2.next
                temp1 = temp1.next
            temp = temp.next
        print(result)
                        
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
obj = LinkedList()
obj.push(-1)
obj.push(0)
obj.push(1)
obj.push(2)
obj.push(-1)
obj.push(-4)
obj.tripleSum()
obj.display()
