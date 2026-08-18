# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # first instict is to use a stack here (FILO)
        if head is None:
            return head

        stack = []
        cur = head
        while cur is not None: # NOT cur.next, which will skip a value
            stack.append(cur)
            cur = cur.next
        head = stack[-1]
        while stack:
            cur = stack.pop()
            if stack:
                cur.next = stack[-1]
        cur.next = None        
        return head