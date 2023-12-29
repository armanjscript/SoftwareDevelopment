class Node:
    
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    
    def __init__(self):
        self.root = None
    

    def insert(self, data):
        
        new_node = Node(data)
        
        if self.root is None:
            self.root = new_node
            return new_node

        else:
            current = self.root
            parent = None
            while True:
                parent = current
                if new_node.data < parent.data:
                    current = current.left
                    if current is None:
                        parent.left = new_node
                        return self.root
                else:
                    current = current.right
                    if current is None:
                        parent.right = new_node
                        return self.root

    def inorder(self, root_node):

        current = root_node

        if current is None:
            return
        
        self.inorder(current.left)
        print(current.data)
        self.inorder(current.right)



tree = Tree()

r=tree.insert(5)
r=tree.insert(3)
r=tree.insert(1)
r=tree.insert(7)
r=tree.insert(9)
r=tree.insert(4)

tree.inorder(r)