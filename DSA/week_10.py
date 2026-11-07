class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def height(self,root):
        if root is None:
            return 0
        return root.height

    def balance(self,root):
        if root is None:
            return 0
        return self.height(root.left)-self.height(root.right)

    def right_rotate(self,y):
        x = y.left
        t = x.right

        x.right = y
        y.left = t

        y.height = 1+max(self.height(y.left),self.height(y.right))
        x.height = 1+max(self.height(x.left),self.height(x.right))

        return x

    def left_rotate(self,x):
        y = x.right
        t = y.left

        y.left = x
        x.right = t

        x.height = 1+max(self.height(x.left),self.height(x.right))
        y.height = 1+max(self.height(y.left),self.height(y.right))

        return y

    def insert(self,root,data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left,data)
        elif data > root.data:
            root.right = self.insert(root.right,data)
        else:
            return root

        root.height = 1+max(self.height(root.left),self.height(root.right))

        b = self.balance(root)

        if b > 1 and data < root.left.data:
            return self.right_rotate(root)

        if b < -1 and data > root.right.data:
            return self.left_rotate(root)

        if b > 1 and data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if b < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def min_value(self,root):
        temp = root
        while temp.left is not None:
            temp = temp.left
        return temp

    def delete(self,root,data):
        if root is None:
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

            temp = self.min_value(root.right)
            root.data = temp.data
            root.right = self.delete(root.right,temp.data)

        root.height = 1+max(self.height(root.left),self.height(root.right))

        b = self.balance(root)

        if b > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        if b > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if b < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        if b < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

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

    def tree_height(self,root):
        if root is None:
            return 0
        return 1+max(self.tree_height(root.left),self.tree_height(root.right))


a = AVL()
root = None

while True:
    print("\n1.Insert")
    print("2.Delete")
    print("3.Inorder")
    print("4.Preorder")
    print("5.Postorder")
    print("6.Count Leaf Nodes")
    print("7.Count Internal Nodes")
    print("8.Height of Tree")
    print("9.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        data = int(input("Enter data: "))
        root = a.insert(root,data)

    elif ch == 2:
        data = int(input("Enter data: "))
        root = a.delete(root,data)

    elif ch == 3:
        a.inorder(root)
        print()

    elif ch == 4:
        a.preorder(root)
        print()

    elif ch == 5:
        a.postorder(root)
        print()

    elif ch == 6:
        print("Leaf Nodes:",a.count_leaf(root))

    elif ch == 7:
        print("Internal Nodes:",a.count_internal(root))

    elif ch == 8:
        print("Height of Tree:",a.tree_height(root))

    elif ch == 9:
        break

    else:
        print("Invalid choice")
