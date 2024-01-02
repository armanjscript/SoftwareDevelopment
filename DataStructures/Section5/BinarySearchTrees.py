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

    def search(self, value):
        if self.root is None:
            print('Tree is empty!')
            return None
        else:
            current = self.root
            while True:
                if value < current.data:
                    current = current.left
                    if current is None:
                        return None
                elif value > current.data:
                    current = current.right
                    if current is None:
                        return None
                else:
                    return current.data
        return None
    
    def get_node_with_parent(self, data):
        parent = None
        current = self.root

        if current is None:
            return (parent, None)
        
        while True:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right
        return (parent, current)
    
    def remove(self, data):

        parent, node = self.get_node_with_parent(data)
        if parent is None and node is None:
            return False
        
        children_count = 0
        if node.left and node.right:
            children_count = 2
        elif (node.left is None) and (node.right is None):
            children_count = 0
        else:
            children_count = 1
        
        if children_count == 0:
            if parent:
                if parent.right is node:
                    parent.right = None
                else:
                    parent.left = None
            else:
                self.root = None
        elif children_count == 1:
            next_node = None
            if node.left:
                next_node = node.left
            else:
                next_node = node.right
            
            if parent:
                 if parent.left is node:
                    parent.left = next_node
                 else:
                    parent.right = next_node
            else:
                self.root = next_node
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right
            while leftmost_node.left:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left
            node.data = leftmost_node.data
            if parent_of_leftmost_node.left == leftmost_node:
                parent_of_leftmost_node.left = leftmost_node.right
            else:
                parent_of_leftmost_node.right = leftmost_node.right
    
    def find_min(self):
        current = self.root
        while current.left:
            current = current.left
        return current.data
    
    def find_max(self):
        current = self.root
        while current.right:
            current = current.right
        return current.data






tree = Tree()

r=tree.insert(5)
r=tree.insert(3)
r=tree.insert(1)
r=tree.insert(7)
r=tree.insert(9)
r=tree.insert(4)
r=tree.insert(8)
tree.remove(5)

tree.inorder(r)

print(f"The element found is: {tree.search(5)}")

print(tree.find_min())
print(tree.find_max())

