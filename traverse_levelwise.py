#traversing tree level wise
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    
    def __init__(self):
        self.root = None
        self.cnt = 0        

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
            return

        temp = self.root
        while True:
            if new_node.data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    return
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return
                temp = temp.right

    def inorder(self, rt):
        if rt is None:
            return
        self.inorder(rt.left)   
        print(rt.data, end=" ")
        self.inorder(rt.right)

    def preorder(self, rt):
        if rt is None:
            return 
        print(rt.data, end=" ")
        self.preorder(rt.left)
        self.preorder(rt.right)

    def postorder(self, rt):
        if rt is None :
            return
        self.postorder(rt.left)
        self.postorder(rt.right)
        print(rt.data, end= " ")

    def level_order(self,rt):
        if rt is None:
            print("BST is empty")
        arr=[]
        cnt = 0
        arr.append(rt)
        while(cnt<len(arr)):
            temp = arr[cnt]
            cnt+=1
            print(temp.data,end = " ")
            if temp.left:
                arr.append(temp.left)
            if temp.right :
                arr.append(temp.right)
    


# --- Driver Code ---
b1 = BST()
for val in [100, 10, 450, 4, 65, 300, 500]:
    b1.insert(Node(val))

print("\nInorder:")
b1.inorder(b1.root)

print("\npreorder:")
b1.preorder(b1.root)

print("\npostorder:")
b1.postorder(b1.root)

print("\nLevel order:")
b1.level_order(b1.root)