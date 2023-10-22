# https://leetcode.com/problems/min-stack/description/

class MinStack:
    # Create a normal stack and a min stack which adds values only if the current value is less equal to the top min stack value
    # Pop from the min stack only if the value popped from the regular stack is equal to the top value of the min stack

    def __init__(self):
        self.stack = []
        self.min_val = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_val:
            self.min_val.append(val)
        else:
            if self.min_val[-1] >= val:
                self.min_val.append(val)

    def pop(self) -> None:
        popped_item = self.stack.pop()
        if self.min_val[-1] == popped_item:
            self.min_val.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_val[-1]
