class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0



queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())  # Output: 10
print(queue.dequeue())  # Output: 20
print(queue.isEmpty())  # Output: False
print(queue.dequeue())  # Output: 30
print(queue.isEmpty())  # Output: True
print(queue.dequeue())  # Output: None (queue is empty, returns None)
