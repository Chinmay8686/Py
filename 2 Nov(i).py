class Stack:
    def __init__(self, capacity=100):
        self.items = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) >= self.capacity

    def push(self, item):
        if self.is_full():
            print("Stack Overflow! Cannot push element.")
            return False
        self.items.append(item)
        print(f"Pushed '{item}' into the stack.")
        return True

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Stack is empty.")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        print("Stack (Top to Bottom):")
        for item in reversed(self.items):
            print(f"| {item} |")
        print("-" * 13)


def reverse_string(input_str):
    """Reverses a string using a Stack."""
    stack = Stack(len(input_str))
    
    for char in input_str:  # Push characters
        stack.push(char)
        
    reversed_str = ""  # Pop characters
    while not stack.is_empty():
        reversed_str += stack.pop()
        
    return reversed_str


def reverse_stack(stack):
    """Reverses a stack using temporary stacks."""
    temp_stack1 = Stack(stack.capacity)
    temp_stack2 = Stack(stack.capacity)
    
    
    while not stack.is_empty():  # Transfer elements from original stack to temp_stack1 (reverses order once)
        temp_stack1.push(stack.pop())
        
   
    while not temp_stack1.is_empty():  # Transfer from temp_stack1 to temp_stack2 (reverses order twice back to original sequence)
        temp_stack2.push(temp_stack1.pop())
        
    
    while not temp_stack2.is_empty(): # Transfer back to original stack so it is fully reversed
        stack.push(temp_stack2.pop())
        
    return stack


if __name__ == "__main__":
    print("--- Basic Stack Operations ---")
    s = Stack(5)
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()
    
    print(f"Popped element: {s.pop()}")
    s.display()
    
    print("\n--- Reverse String using Stack ---")
    original_text = "DataStructures"
    print(f"Original String: {original_text}")
    print(f"Reversed String: {reverse_string(original_text)}")

    print("\n--- Reverse Stack using Another Stack ---")
    print("Original Stack before reversal:")
    s.display()
    
    reverse_stack(s)
    
    print("Stack after reversal:")
    s.display()