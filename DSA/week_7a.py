class Stack:
    def __init__(self):
        self.stack = []
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Deleted element:",self.stack.pop())
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Top element:",self.stack[-1])
    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print(self.stack[::-1])
s = Stack()
while True:
    print("\n1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display")
    print("5.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        data = int(input("Enter element: "))
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
