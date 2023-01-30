#138. Copy List with Random Pointer
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Solution With Approach 1
        if head is None:
            return head
        iter = head
        while(iter):
            newNode = Node(iter.val,iter.next)
            iter.next = newNode
            iter = newNode.next
        iter = head
        while(iter):
            if iter.random is not None:
                iter.next.random = iter.random.next
            iter = iter.next.next
        iter = head
        while(iter and iter.next):
            newpointer = iter.next
            if iter.next.next is not None:
                nextpointer = iter.next.next
                iter.next.next = iter.next.next.next
            iter = newpointer
        return head.next

        #Solution With Approach 2
        '''
        if head is None:
            return head
        data = dict()
        temp = head
        while(temp):
            newNode = Node(temp.val)
            data[temp] = newNode
            temp = temp.next
        temp = head
        while(temp):
            if temp.next is not None:
                data[temp].next = data[temp.next]
            if temp.random is not None:
                data[temp].random = data[temp.random]
            temp = temp.next
        return data[head]
        '''
