class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,root,data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left,data)
        elif data > root.data:
            root.right = self.insert(root.right,data)
        return root

    def delete(self,root,data):
        if root is None:
            print("Value not found")
            return root
        if data < root.data:
            root.left = self.delete(root.left,data)
        elif data > root.data:
            root.right = self.delete(root.right,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = root.right
            while temp.left is not None:
                temp = temp.left
            root.data = temp.data
            root.right = self.delete(root.right,temp.data)
        return root

    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)

    def preorder(self,root):
        if root is not None:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")

    def count_leaf(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.count_leaf(root.left)+self.count_leaf(root.right)

    def count_internal(self,root):
        if root is None or (root.left is None and root.right is None):
            return 0
        return 1+self.count_internal(root.left)+self.count_internal(root.right)

    def height(self,root):
        if root is None:
            return 0
        return 1+max(self.height(root.left),self.height(root.right))


b = BST()

while True:
    print("\n1.Insert")
    print("2.Delete")
    print("3.Inorder")
    print("4.Preorder")
    print("5.Postorder")
    print("6.Count Leaf Nodes")
    print("7.Count Internal Nodes")
    print("8.Height")
    print("9.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        data = int(input("Enter data: "))
        b.root = b.insert(b.root,data)

    elif ch == 2:
        data = int(input("Enter data: "))
        b.root = b.delete(b.root,data)

    elif ch == 3:
        b.inorder(b.root)
        print()

    elif ch == 4:
        b.preorder(b.root)
        print()

    elif ch == 5:
        b.postorder(b.root)
        print()

    elif ch == 6:
        print("Leaf Nodes:",b.count_leaf(b.root))

    elif ch == 7:
        print("Internal Nodes:",b.count_internal(b.root))

    elif ch == 8:
        print("Height of Tree:",b.height(b.root))

    elif ch == 9:
        break

    else:
        print("Invalid choice")
