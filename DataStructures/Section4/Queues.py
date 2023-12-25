
class Node(object):
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    

class Queue:
    
    def __init__(self):
        
        self.head = None
        self.tail = None
        self.count = 0
    
    def enqueue(self, data):
        
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count +=1
    
    def dequeue(self):
        
        if self.count ==1:
            self.head = None
            self.tail = None
        
        elif self.count>1:
            self.count -=1
            self.head = self.head.next
            self.head.prev = None

        elif self.count < 1:
            print('Queue is empty!')
            return
        self.count-=1
    
    def iter(self):

        current = self.head

        while current:
            val = current.data
            current = current.next
            yield val



queue = Queue()
queue.enqueue('Python')
queue.enqueue('C++')
queue.enqueue('JavaScript')

for item in queue.iter():
    print(item)

