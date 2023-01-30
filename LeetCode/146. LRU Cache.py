#146. LRU Cache

#Approach 1
class Node:
    def __init__(self,data,value):
        self.data = data
        self.value = value
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.data = dict()
        self.capacity = capacity
        self.headNode = Node(0,0)
        self.tailNode = Node(0,0)
        self.headNode.next = self.tailNode
        self.tailNode.prev = self.headNode
    def get(self, key: int) -> int:
        if key in self.data:
            self.put(key,self.data[key].value)
            return self.data[key].value
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data[key].prev.next = self.data[key].next
            self.data[key].next.prev = self.data[key].prev
            del self.data[key]
        elif len(self.data) >= self.capacity:
            dummykey = self.tailNode.prev.data
            self.tailNode.prev.prev.next = self.tailNode
            self.tailNode.prev = self.tailNode.prev.prev
            del self.data[dummykey]
        newNode = Node(key,value)
        newNode.prev = self.headNode
        newNode.next = self.headNode.next
        self.headNode.next = newNode
        newNode.next.prev = newNode
        self.data[key] = newNode
obj = LRUCache(2)
print(obj.put(1,1))
print(obj.put(2,2))
print(obj.get(1))
print(obj.put(3,3))
print(obj.get(2))
print(obj.put(4,4))
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))


#Approach 2    
'''
# LRU BY Ordered Dict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        else:
            self.values[key] = self.values.pop(key)
            return self.values[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.values:
            if len(self.values) == self.capacity:
                self.values.popitem(last=False)
        else:
            self.values.pop(key)
        self.values[key] = value
'''
