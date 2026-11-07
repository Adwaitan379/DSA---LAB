class Heap:
    def __init__(self):
        self.heap = []
        self.type = ""

    def insert(self,data):
        self.heap.append(data)
        i = len(self.heap)-1

        while i > 0:
            p = (i-1)//2

            if self.type == "max" and self.heap[i] > self.heap[p]:
                self.heap[i],self.heap[p] = self.heap[p],self.heap[i]
            elif self.type == "min" and self.heap[i] < self.heap[p]:
                self.heap[i],self.heap[p] = self.heap[p],self.heap[i]
            else:
                break

            i = p

    def delete(self):
        if len(self.heap) == 0:
            print("Heap is empty")
            return

        print("Deleted root:",self.heap[0])

        if len(self.heap) == 1:
            self.heap.pop()
            return

        self.heap[0] = self.heap.pop()
        i = 0
        n = len(self.heap)

        while True:
            left = 2*i+1
            right = 2*i+2
            largest = i

            if self.type == "max":
                if left < n and self.heap[left] > self.heap[largest]:
                    largest = left
                if right < n and self.heap[right] > self.heap[largest]:
                    largest = right

            else:
                if left < n and self.heap[left] < self.heap[largest]:
                    largest = left
                if right < n and self.heap[right] < self.heap[largest]:
                    largest = right

            if largest == i:
                break

            self.heap[i],self.heap[largest] = self.heap[largest],self.heap[i]
            i = largest

    def display(self):
        if len(self.heap) == 0:
            print("Heap is empty")
        else:
            print("Heap:",self.heap)


while True:
    print("\n1.Max Heap")
    print("2.Min Heap")
    print("3.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1 or ch == 2:
        h = Heap()

        if ch == 1:
            h.type = "max"
        else:
            h.type = "min"

        while True:
            print("\n1.Insert")
            print("2.Delete Root")
            print("3.Display")
            print("4.Back to Main Menu")

            op = int(input("Enter choice: "))

            if op == 1:
                data = int(input("Enter element: "))
                h.insert(data)

            elif op == 2:
                h.delete()

            elif op == 3:
                h.display()

            elif op == 4:
                break

            else:
                print("Invalid choice")

    elif ch == 3:
        break

    else:
        print("Invalid choice")
