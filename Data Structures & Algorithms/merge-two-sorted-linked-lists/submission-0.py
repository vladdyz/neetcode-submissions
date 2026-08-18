# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # BRUTE FORCE APPROACH
        mergedArr = []
        curr = list1
        while curr:
            mergedArr.append(curr.val)
            curr = curr.next
        curr = list2
        while curr:
            mergedArr.append(curr.val)
            curr = curr.next
        mergedArr.sort()

        head = None
        prev = None

        for val in mergedArr:
            node = ListNode(val)
            if prev:
                prev.next = node
            prev = node
            if head is None:
                head = node
        return head

        
        
        # curr, prev = None
        # if list1 and 

