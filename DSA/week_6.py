class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_begin(self,data):
        x = Node(data)
        if self.head is None:
            self.head = self.tail = x
        else:
            x.next = self.head
            self.head.prev = x
            self.head = x

    def insert_end(self,data):
        x = Node(data)
        if self.head is None:
            self.head = self.tail = x
        else:
            x.prev = self.tail
            self.tail.next = x
            self.tail = x

    def insert(self,data,ind):
        if ind < 0:
            print("Enter valid index")
            return
        if ind == 0:
            return self.insert_begin(data)
        x = Node(data)
        temp = self.head
        for i in range(ind-1):
            if temp is None:
                print("Enter valid index")
                return
            temp = temp.next
        if temp is None:
            print("Enter valid index")
            return
        x.prev = temp
        x.next = temp.next
        if temp.next is not None:
            temp.next.prev = x
        else:
            self.tail = x
        temp.next = x

    def delete_begin(self):
        if self.head is None:
            print("List is empty")
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_end(self):
        if self.head is None:
            print("List is empty")
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def delete_val(self,val):
        temp = self.head
        while temp is not None:
            if temp.data == val:
                if temp == self.head:
                    return self.delete_begin()
                elif temp == self.tail:
                    return self.delete_end()
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    return
            temp = temp.next
        print("Value not found")

    def count(self):
        c = 0
        temp = self.head
        while temp is not None:
            c += 1
            temp = temp.next
        print("Count =",c)

    def display(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while temp is not None:
            print(temp.data,end=" <-> ")
            temp = temp.next
        print("None")

    def display_reverse(self):
        temp = self.tail
        if temp is None:
            print("List is empty")
            return
        while temp is not None:
            print(temp.data,end=" <-> ")
            temp = temp.prev
        print("None")

d = DLL()

while True:
    print("\n1.Insert begin")
    print("2.Insert end")
    print("3.Insert at index")
    print("4.Delete begin")
    print("5.Delete end")
    print("6.Delete by value")
    print("7.Count")
    print("8.Display")
    print("9.Display reverse")
    print("10.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        data = int(input("Enter data: "))
        d.insert_begin(data)
    elif ch == 2:
        data = int(input("Enter data: "))
        d.insert_end(data)
    elif ch == 3:
        data = int(input("Enter data: "))
        ind = int(input("Enter index: "))
        d.insert(data,ind)
    elif ch == 4:
        d.delete_begin()
    elif ch == 5:
        d.delete_end()
    elif ch == 6:
        val = int(input("Enter value: "))
        d.delete_val(val)
    elif ch == 7:
        d.count()
    elif ch == 8:
        d.display()
    elif ch == 9:
        d.display_reverse()
    elif ch == 10:
        break
    else:
        print("Invalid choice")
