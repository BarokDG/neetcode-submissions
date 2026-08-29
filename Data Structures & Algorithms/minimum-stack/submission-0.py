class MinStack:

    def __init__(self):
        self.minimum = []
        self.stack = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)

        if len(self.minimum) == 0 or (value <= self.minimum[-1]):
            self.minimum.append(value)

    def pop(self) -> None:
        top = self.stack.pop()

        if len(self.minimum) != 0 and top == self.minimum[-1]:
            self.minimum.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum[-1] if self.minimum else None
        
