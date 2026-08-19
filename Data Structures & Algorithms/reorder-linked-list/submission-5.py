# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reordering a list -> stack?
        # dont touch the head - staya where it is
        if head is None or head.next is None:
            return 
        stack = []
        curr = head
        while (curr):
            stack.append(curr)
            curr = curr.next
        
        # last element is at the top of the stack, first element (head) should be removed (dont touch its position)
        stack.pop(0)
        prev = stack.pop() # also keep track of the previous node for the following loop
        head.next = prev
        # print(head.next.val)
        # print(stack[-1].val)
        # print(stack[-2].val)

        # UPDATE. This expects stack[0] -> stack[-1] -> stack[1] -> stack[-2]... etc
        # Refactored this annoying problem to use a flag...
        flip = True # either pop from the end of the list or from the beginning

        while len(stack) > 0: # ignore the last element
            if flip:
                curr = stack.pop(0)
                flip = False
            else:
                curr = stack.pop()
                flip = True
            # print(curr.val)
            prev.next = curr
            prev = curr
        
        # the last element should point to nothing to prevent a loop
        if curr:
            curr.next = None
       


        