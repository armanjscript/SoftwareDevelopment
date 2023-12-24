class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None




class Stack:
    
    def __init__(self):
        self.top = None
        self.size = 0

    
    def push(self,data):
        new_node = Node(data)

        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        
        self.size+=1
    
    def pop(self):
        if self.top:
            data = self.top.data
            self.size -=1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            print('Stack is empty!')
    
    
    def iter(self):
        if self.top is None:
            print('No items in the stack')
            return
        else:
            current = self.top
            while current:
                val = current.data
                current = current.next
                yield val
    
    def peek(self):
        if self.top:
            return self.top.data
        else:
            print('Stack is empty!')
    

stack = Stack()
stack.push('Python')
stack.push('C++')
stack.push('C#')
stack.push('Javascript')

for lang in stack.iter():
    print(lang)

stack.pop()

print("====================")
for lang in stack.iter():
    print(lang)

print("-========")
print(stack.peek())


