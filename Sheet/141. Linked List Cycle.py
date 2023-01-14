#141. Linked List Cycle
def hasCycle(self, head: Optional[ListNode]) -> bool:
        result = False
        slow = fast = head
        while(slow is not None and fast is not None):
            slow = slow.next
            if fast.next is not None:
                fast = fast.next.next
            else:
                return False
            if slow == fast:
                return True
            
        return result
