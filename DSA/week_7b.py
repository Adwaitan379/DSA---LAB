class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def push(self,data):
        x = Node(data)
        x.next = self.top
        self.top = x
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Deleted element:",self.top.data)
            self.top = self.top.next
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:",self.top.data)

    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top
            while temp is not None:
                print(temp.data)
                temp = temp.next
s = Stack()
while True:
    print("\n1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display")
    print("5.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        data = int(input("Enter data: "))
        s.push(data)
    elif ch == 2:
        s.pop()
    elif ch == 3:
        s.peek()
    elif ch == 4:
        s.display()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
