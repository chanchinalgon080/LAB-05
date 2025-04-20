class QueueWithStacks:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, value):
        self.stack_enqueue.append(value)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        
        return self.stack_dequeue.pop()

    def peek(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        
        return self.stack_dequeue[-1]

    def isEmpty(self):
        return not self.stack_enqueue and not self.stack_dequeue

    def size(self):
        return len(self.stack_enqueue) + len(self.stack_dequeue)

print("Test Case 1:")
q1 = QueueWithStacks()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
print("Dequeue:", q1.dequeue())  # Expected: 1
print("Peek:", q1.peek())        # Expected: 2
print("Size:", q1.size())        # Expected: 2
print()

print("Test Case 2:")
q2 = QueueWithStacks()
print("Is empty?", q2.isEmpty())  # Expected: True
q2.enqueue(5)
print("Is empty after enqueue?", q2.isEmpty())  # Expected: False
print("Size:", q2.size())                       # Expected: 1
print()

print("Test Case 3:")
q3 = QueueWithStacks()
q3.enqueue(100)
q3.enqueue(200)
print("Dequeue:", q3.dequeue())  # Expected: 100
q3.enqueue(300)
print("Dequeue:", q3.dequeue())  # Expected: 200
print("Dequeue:", q3.dequeue())  # Expected: 300
print("Is empty?", q3.isEmpty()) # Expected: True
