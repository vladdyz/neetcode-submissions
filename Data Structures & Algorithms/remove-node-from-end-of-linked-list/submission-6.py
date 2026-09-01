# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head # edge case
        length = 1
        curr = head
        # first pass: check the length of the list
        while curr.next:
            curr = curr.next
            length += 1
        if length == 1 and n == 1:
            return None
        if length == n:
            head = head.next
            return head

        removedElement = length - n
        # second pass: find the nth element to remove
        currentIdx = 1
        curr = head.next
        prev = head
        while curr:
            if currentIdx == removedElement:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
            currentIdx += 1
        #print(length)
        #print(currentIdx)
        
        return head


        