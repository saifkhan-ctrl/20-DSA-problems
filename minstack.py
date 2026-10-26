class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)

        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            raise IndexError("Stack is empty")

        value = self.stack.pop()

        if value == self.min_stack[-1]:
            self.min_stack.pop()

        return value

    def top(self):
        if not self.stack:
            raise IndexError("Stack is empty")

        return self.stack[-1]

    def get_min(self):
        if not self.min_stack:
            raise IndexError("Stack is empty")

        return self.min_stack[-1]


# Example usage
s = MinStack()

s.push(5)
s.push(3)
s.push(7)

print("Minimum:", s.get_min())  # 3
print("Top:", s.top())          # 7

s.pop()
print("Minimum:", s.get_min())  # 3

s.pop()
print("Minimum:", s.get_min())  # 5