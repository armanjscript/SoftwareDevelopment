
from collections import deque


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

def levelorder(root_node):

    traversing_nodes = deque([root_node])
    list_of_nodes = []
    while len(traversing_nodes) > 0:
        node = traversing_nodes.popleft()
        list_of_nodes.append(node.data)
        if node.left:
            traversing_nodes.append(node.left)
        if node.right:
            traversing_nodes.append(node.right)
    return list_of_nodes


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

print("=======================")

for item in levelorder(n1):
    print(item)

print("*===================*")

class Stack:
    
    def __init__(self):
        self.elements = []

    def push(self, data):
        self.elements.append(data)
    
    def pop(self):
        return self.elements.pop()

class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

#calculation of expr

expr = "4 5 + 5 3 - *".split()
stack = Stack()

for term in expr:
    if term in "*/+-":
        node = TreeNode(term)
        node.right = stack.pop()
        node.left = stack.pop()
    else:
        node = TreeNode(int(term))
    
    stack.push(node)

def calc(node):
    if node.data == "+":
        return calc(node.left) + calc(node.right)
    elif node.data == "-":
        return calc(node.left) - calc(node.right)
    elif node.data == "/":
        return calc(node.left) // calc(node.right)
    elif node.data == "*":
        return calc(node.left) * calc(node.right)
    else:
        return node.data

root = stack.pop()
result = calc(root)
print(f"The result of expression is : {result}")