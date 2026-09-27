class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Test Case 1
s = MinStack()
s.push(-2)
s.push(0)
s.push(-3)
print("Test Case 1:", s.getMin())
s.pop()
print("After pop:", s.top())

# Test Case 2 - Edge case
s2 = MinStack()
s2.push(5)
print("Test Case 2:", s2.getMin())