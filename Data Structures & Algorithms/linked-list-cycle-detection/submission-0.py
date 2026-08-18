# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mySet = set()

        while head is not None:
            if head not in mySet:
                mySet.add(head)
            else:
                return True
            head = head.next

        # for node in mySet:
        #     if node != head:
        #         return True
        #     head = head.next
        return False


