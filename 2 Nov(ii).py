class LinearQueue:
    def __init__(self, capacity=100):
        self.items = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) >= self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("Queue Overflow! Cannot enqueue.")
            return False
        self.items.append(item)
        print(f"Enqueued: {item}")
        return True

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Queue is empty.")
            return None
        return self.items.pop(0)

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue (Front to Rear):", " <- ".join(str(x) for x in self.items))


def reverse_queue(q):
    """Reverses a linear queue using a temporary stack."""
    stack = []
    
  
    while not q.is_empty():
        stack.append(q.dequeue())
        
    # Move back to queue (stack pop reverses the order)
    while stack:
        q.enqueue(stack.pop())
        
    return q


def merge_queues(q1, q2):
    """Merges two queues into a new queue."""
    merged_capacity = q1.capacity + q2.capacity
    merged_q = LinearQueue(merged_capacity)
    
    for item in q1.items:
        merged_q.enqueue(item)
        
    for item in q2.items:
        merged_q.enqueue(item)
        
    return merged_q


def are_identical(q1, q2):
    """Checks if two queues have the exact same elements in the same order."""
    if len(q1.items) != len(q2.items):
        return False
    return q1.items == q2.items


if __name__ == "__main__":
    print("--- Basic Queue Operations ---")
    q1 = LinearQueue(5)
    q1.enqueue(10)
    q1.enqueue(20)
    q1.enqueue(30)
    q1.display()

    print(f"\nDequeued: {q1.dequeue()}")
    q1.display()

    print("\n--- Reverse Queue using Stack ---")
    print("Before reversal:")
    q1.display()
    reverse_queue(q1)
    print("After reversal:")
    q1.display()

    print("\n--- Check Identical & Merge Queues ---")
    q2 = LinearQueue(5)
    q2.enqueue(30)
    q2.enqueue(10)

    q3 = LinearQueue(5)
    q3.enqueue(30)
    q3.enqueue(10)

    print("Are q2 and q3 identical?", are_identical(q2, q3))

    q_merged = merge_queues(q1, q2)
    print("Merged Queue (q1 + q2):")
    q_merged.display()