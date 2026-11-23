class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, newnode):
        if self.root is None:  # BST is empty
            self.root = newnode  # First Node
        else:
            temp = self.root
            while True:
                if newnode.data < temp.data:
                    if temp.left is None:
                        temp.left = newnode
                        return
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = newnode
                        return
                    else:
                        temp = temp.right

    def del_node(self, rt, val):
        if rt is None:
            return None

        if val < rt.data:
            rt.left = self.del_node(rt.left, val)
        elif val > rt.data:
            rt.right = self.del_node(rt.right, val)
        else:
            # Node with only one child or no child
            if rt.left is None:
                return rt.right
            if rt.right is None:
                return rt.left

            # Node with both left and right children
            succ = self.get_successor(rt)
            rt.data = succ.data
            rt.right = self.del_node(rt.right, succ.data)

        return rt

    def delete(self, val):
        self.root = self.del_node(self.root, val)

    def get_successor(self, temp):
        temp = temp.right
        while temp is not None and temp.left is not None:
            temp = temp.left
        return temp

    def inorder(self, rt):
        if rt is None:
            return
        self.inorder(rt.left)
        print(rt.data, end="  ")
        self.inorder(rt.right)

    def preorder(self, rt):
        if rt is None:
            return
        print(rt.data, end="  ")
        self.preorder(rt.left)
        self.preorder(rt.right)

    def postorder(self, rt):
        if rt is None:
            return
        self.postorder(rt.left)
        self.postorder(rt.right)
        print(rt.data, end="  ")

    def minimum(self):
        if self.root is None:
            print("Tree is empty")
            return
        temp = self.root
        while temp.left is not None:
            temp = temp.left
        print("Minimum value:", temp.data)

    def maximum(self):
        if self.root is None:
            print("Tree is empty")
            return
        temp = self.root
        while temp.right is not None:
            temp = temp.right
        print("Maximum value:", temp.data)


b = BST()
b.insert(Node(20))
b.insert(Node(30))
b.insert(Node(10))
b.insert(Node(5))

print("In Order:")
b.inorder(b.root)

print("\nPre Order:")
b.preorder(b.root)

print("\nPost Order:")
b.postorder(b.root)
print()