class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [[] for i in range(size)]

    def insert(self,key):
        index = key % self.size
        self.table[index].append(key)

    def display(self):
        for i in range(self.size):
            print(i,":",self.table[i])

h = HashTable(10)

while True:
    print("\n1.Insert")
    print("2.Display")
    print("3.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        key = int(input("Enter key: "))
        h.insert(key)
    elif ch == 2:
        h.display()
    elif ch == 3:
        break
    else:
        print("Invalid choice")
