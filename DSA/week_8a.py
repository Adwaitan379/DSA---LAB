class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Deleted element:",self.queue.pop(0))
    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Front element:",self.queue[0])
    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print(self.queue)
q = Queue()
while True:
    print("\n1.Enqueue")
    print("2.Dequeue")
    print("3.Peek")
    print("4.Display")
    print("5.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        data = int(input("Enter data: "))
        q.enqueue(data)
    elif ch == 2:
        q.dequeue()
    elif ch == 3:
        q.peek()
    elif ch == 4:
        q.display()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
