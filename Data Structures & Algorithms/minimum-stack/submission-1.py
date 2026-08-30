class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)

        next_min = min(
            value, 
            self.min_stack[-1] if self.min_stack else value
        )
        self.min_stack.append(next_min)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
