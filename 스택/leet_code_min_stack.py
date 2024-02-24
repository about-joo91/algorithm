class MinStack:
    INF = int(10e9)

    def __init__(self):
        self.stack = []
        self.min = MinStack.INF
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min = min(self.min, val)
        

    def pop(self) -> None:
        if self.stack:
            top_value = self.stack.pop()
            if top_value == self.min:
                self.min = min(self.stack) if self.stack else MinStack.INF

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return None if self.min == MinStack.INF else self.min
        
