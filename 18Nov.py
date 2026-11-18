
class Process:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.queue = []

    # Add Process
    def enqueue(self, pid, name, priority):
        if priority < 1 or priority > 4:
            print("Invalid Priority!")
            return

        process = Process(pid, name, priority)
        self.queue.append(process)
        print("Process Added Successfully!")

    # Execute Process
    def dequeue(self):
        if len(self.queue) == 0:
            print("No Process Available!")
            return

        highest = min(self.queue, key=lambda p: p.priority)
        self.queue.remove(highest)

        print("Executing Process:")
        print("Process ID:", highest.pid)
        print("Process Name:", highest.name)
        print("Priority:", highest.priority)

    # View Next Process
    def display_next(self):
        if len(self.queue) == 0:
            print("No Pending Process!")
            return

        highest = min(self.queue, key=lambda p: p.priority)

        print("Next Process to Execute:")
        print("Process ID:", highest.pid)
        print("Process Name:", highest.name)
        print("Priority:", highest.priority)

    # Display All Processes
    def display_all(self):
        if len(self.queue) == 0:
            print("No Pending Processes!")
            return

        print("\nPending Processes:")
        sorted_queue = sorted(self.queue, key=lambda p: p.priority)

        for p in sorted_queue:
            print("ID:", p.pid, "| Name:", p.name,
                  "| Priority:", p.priority)

    # Count Processes
    def count(self):
        print("Total Pending Processes:", len(self.queue))


# Main Program
pq = PriorityQueue()

while True:
    print("\n--- CPU PROCESS SCHEDULING ---")
    print("1. Add Process")
    print("2. Execute Process")
    print("3. View Next Process")
    print("4. Display All Processes")
    print("5. Count Processes")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        pid = int(input("Enter Process ID: "))
        name = input("Enter Process Name: ")
        priority = int(input("Enter Priority (1-4): "))
        pq.enqueue(pid, name, priority)

    elif choice == 2:
        pq.dequeue()

    elif choice == 3:
        pq.display_next()

    elif choice == 4:
        pq.display_all()

    elif choice == 5:
        pq.count()

    elif choice == 6:
        print("Exiting Program...")
        break
                            
    else:
        print("Invalid Choice! Try Again.")
