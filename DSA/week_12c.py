class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [None]*size

    def insert(self,key):
        index = key % self.size

        for i in range(self.size):
            new_index = (index+i*i)%self.size

            if self.table[new_index] is None:
                self.table[new_index] = key
                return

        print("Cannot insert element")

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
