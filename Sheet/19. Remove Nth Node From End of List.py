#19. Remove Nth Node From End of List

#Approach 1 with Time Complexity O(n)
start = ListNode()
start.next = head
slow = fast = start
for i in range(n):
    fast = fast.next
while(fast.next is not None):
    slow = slow.next
    fast = fast.next
slow.next = slow.next.next
return start.next

#Approach 2 with Time Complexity O(n+n)
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        head2 = head
        while(head is not None):
            length+=1
            head = head.next
        
        if length == 1:
            head = None
            return head
        if length == n:
            head = temp.next
            return head
        length = length - n
        i = 1
        while(i<length):
            temp = temp.next
            i+=1
        if temp.next.next:
            temp.next = temp.next.next
        else:
            temp.next = None
        return head2
