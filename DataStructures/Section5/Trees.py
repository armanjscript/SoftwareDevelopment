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

def preorder(root_node):

    current = root_node
    if current is None:
        return
    print(current.data)
    preorder(current.left)
    preorder(current.right)

def postorder(root_node):

    current = root_node
    if current is None:
        return
    postorder(current.left)
    postorder(current.right)
    print(current.data)


n1 = Node('A')
n2 = Node('B')
n3 = Node('C')
n4 = Node('D')
n5 = Node('E')
n6 = Node('F')

n1.left = n2
n2.left = n3
n2.right = n4
n1.right = n5
n5.right = n6

inorder(n1)

print("=======================")

preorder(n1)

print("=======================")

postorder(n1)

