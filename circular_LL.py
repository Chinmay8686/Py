class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Function to add a node at the end of the list
    def append(self, data):
        new_node = Node(data)
        
        # If the list is empty, make the new node point to itself
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        # Otherwise, traverse until we find the node whose next is the head
        current = self.head
        while current.next != self.head:
            current = current.next
            
        current.next = new_node
        new_node.next = self.head

    # Function to display the circular linked list
    def display(self):
        if not self.head:
            print("The list is empty.")
            return
        
        current = self.head
        elements = []
        
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break
                
        print(" -> ".join(elements) + " -> (Points back to Head)")

# --- Example Usage ---
if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append(10)
    cll.append(20)
    cll.append(30)
    cll.append(40)
    
    cll.display()