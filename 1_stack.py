class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0



stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())  # Output: 30
print(stack.pop())  # Output: 20
print(stack.isEmpty())  # Output: False
print(stack.pop())  # Output: 10
print(stack.isEmpty())  # Output: True
print(stack.pop())  # Output: None (stack is empty, returns None)
