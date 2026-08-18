class MinStack:

    def __init__(self):
        # I have a habit of defaulting to "this" when its "self" in Python
        self.stack = []
        # I cant sort the stack in the push method because it destroys the insert order
        # so this stack class must contain TWO stacks (!)
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            if val <= self.min_stack[0]:
                self.min_stack.insert(0, val)
        else:
            self.min_stack.append(val)
        
        #self.stack.sort()
        

    def pop(self) -> None:
        if self.stack:
            popped = self.stack.pop()
            if popped == self.min_stack[0]:
                self.min_stack.remove(popped)



    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[0]
        return None
