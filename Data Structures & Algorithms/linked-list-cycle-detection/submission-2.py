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

        # the optimal solution would be something like
        #   if head == None:
        #         return False
            
        #     slow = head
        #     fast = head

        #     while fast and fast.next :
                    
        #         slow = slow.next
        #         fast = fast.next.next

        #         if slow == fast:
        #                return True


        #     return False

        # another funny solution would be to add/subtract an out-of-range number to each visited value (e.g. + 100,000 or -100,000) and immediately upon visiting a node, check if the value is at least 100000/-100000 to easily identify a loop. Setting the value instead of performing arithmetic works also but at least this way we can always restore the initial values of the visited nodes which is not possible if they're just set to a fixed value instead.

