class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,data):
        x = Node(data)
        if self.rear is None:
            self.front = self.rear = x
        else:
            self.rear.next = x
            self.rear = x

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Deleted element:",self.front.data)
            self.front = self.front.next
            if self.front is None:
                self.rear = None

    def peek(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Front element:",self.front.data)

    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp = self.front
            while temp is not None:
                print(temp.data,end=" -> ")
                temp = temp.next
            print("None")

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
