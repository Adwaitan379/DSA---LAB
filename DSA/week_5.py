class Node:
    def __init__(self,data):
        self.next = None
        self.data = data
class SLL:
    def __init__(self):
        self.head =  None
    def insert_begin(self,data):
        x = Node(data)
        x.next = self.head
        self.head = x
    def insert_end(self,data):
        x = Node(data)
        if self.head is None:
            self.head = x
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = x
    def delete_begin(self):
        if self.head is None:
            print("No data to delete")
        else:
            self.head = self.head.next
    def delete_end(self):
        if self.head is None:
            print("No data to delete")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None
    def display(self):
        if self.head is None:
            print("No data to display")
        else:
            temp = self.head
            while temp:
                print(temp.data,end="->")
                temp = temp.next
            print(None)
    def insert(self,data,ind):
        x = Node(data)
        if ind==0:
            return self.insert_begin(data)
        else:
            temp = self.head
            for i in range(ind-1):
                if temp is None:
                    print("Enter valid index")
                    return
                temp = temp.next
            if temp is None:
                print("Enter valid index")
            else:
                x.next = temp.next
                temp.next = x
    def delete(self,data):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == data:
            return self.delete_begin()
        temp = self.head
        while temp.next and temp.next.data!=data:
            temp = temp.next
        if temp.next is None:
            print("Element not found")
        else:
            temp.next = temp.next.next
    def count(self):
        if self.head is None:
            print("No data to display")
        else:
            c=0
            temp = self.head
            while temp:
                c+=1
                temp = temp.next
            return c

my_list = SLL()
while True:
    print("\n--- Singly Linked List Menu ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Index")
    print("4. Delete from Beginning")
    print("5. Delete from End")
    print("6. Delete by Value")
    print("7. Count Elements")
    print("8. Display List")
    print("9. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        val = int(input("Enter data to insert: "))
        my_list.insert_begin(val)
    elif choice == 2:
        val = int(input("Enter data to insert: "))
        my_list.insert_end(val)
    elif choice == 3:
        val = int(input("Enter data to insert: "))
        ind = int(input("Enter index: "))
        my_list.insert(val, ind)
    elif choice == 4:
        my_list.delete_begin()
    elif choice == 5:
        my_list.delete_end()
    elif choice == 6:
        val = int(input("Enter value to delete: "))
        my_list.delete(val)
    elif choice == 7:
        c = my_list.count()
        if c > 0:
            print("Total elements:", c)
    elif choice == 8:
        my_list.display()
    elif choice == 9:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
