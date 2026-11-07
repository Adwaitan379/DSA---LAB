class CQueue:
    def __init__(self,size):
        self.size = size
        self.queue = [None]*size
        self.front = -1
        self.rear = -1

    def enqueue(self,data):
        if (self.rear+1)%self.size == self.front:
            print("Queue is full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear+1)%self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("Deleted element:",self.queue[self.front])
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front+1)%self.size

    def peek(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("Front element:",self.queue[self.front])

    def display(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            i = self.front
            while True:
                print(self.queue[i],end=" ")
                if i == self.rear:
                    break
                i = (i+1)%self.size
            print()

size = int(input("Enter queue size: "))
q = CQueue(size)

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
