class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None




#traversing the tree

def inorder(root_node):
    
    current = root_node
    if current is None:
        return
    inorder(current.left)
    print(current.data)
    inorder(current.right)


n1 = Node('A')
n2 = Node('B')
n3 = Node('C')
n4 = Node('D')
n5 = Node('E')
n6 = Node('F')

n1.lef = n2
n2.left = n3
n2.right = n4
n1.right = n5
n5.right = n6

inorder(n1)

