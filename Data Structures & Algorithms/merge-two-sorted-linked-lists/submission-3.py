# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # BRUTE FORCE APPROACH
        # mergedArr = []
        # curr = list1
        # while curr:
        #     mergedArr.append(curr.val)
        #     curr = curr.next
        # curr = list2
        # while curr:
        #     mergedArr.append(curr.val)
        #     curr = curr.next
        # mergedArr.sort() # O(n+m log(n+m))

        # head = None
        # prev = None

        # for val in mergedArr:
        #     node = ListNode(val)
        #     if prev:
        #         prev.next = node
        #     prev = node
        #     if head is None:
        #         head = node
        # return head

        # Trying to not brute force it

        # edge case
        if list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        elif not list1 and not list2:
            return None
        currL1 = list1
        currL2 = list2
        # set the head
        if currL1.val < currL2.val:
            head = currL1
            currL1 = currL1.next
        else:
            head = currL2
            currL2 = currL2.next
        prev = head
        while currL1 is not None and currL2 is not None:
            if currL1.val <= currL2.val:
                prev.next = currL1
                prev = currL1
                currL1 = currL1.next
            else:
                prev.next = currL2
                prev = currL2
                currL2 = currL2.next
        
        if currL1 is not None:
            prev.next = currL1
        if currL2 is not None:
            prev.next = currL2
        return head

