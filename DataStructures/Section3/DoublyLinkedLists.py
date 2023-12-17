class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def append_at_start(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count+=1
    
    def append(self, data):

        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count+=1     
    
    def append_loc(self, data, index):

        current = self.head
        prev = self.head
        counter = 0
        
        if index < 0:
            print('Negative indices are impossible!!')
            return
        elif index == 0:
            self.append_at_start(data)
            return
        elif index > self.count - 1:
            print('Indexing out of bounds')
            return
        else:
            while current:
                if index == counter:
                    new_node = Node(data, None, None)
                    new_node.prev = prev
                    new_node.next = current
                    current.prev = new_node
                    prev.next = new_node
                    self.count+=1
                prev = current
                current = current.next
                counter+=1
    
    def iter(self):
        current = self.head
        if self.head is not None:
            while current:
                val = current.data
                current = current.next
                yield val
    
    def reverse(self):
        current = self.tail
        if self.tail is not None:
            while current:
                val = current.data
                current = current.prev
                yield val
    
    def contains(self, data):
        for node in self.iter():
            if node == data:
                return True
        return False


    

            






dbl_list = DoublyLinkedList()
dbl_list.append('Python')
dbl_list.append('C++')
dbl_list.append_at_start('Javascript')
dbl_list.append_loc('MySql', 0)


for item in dbl_list.iter():
    print(item)

for item in dbl_list.reverse():
    print(item)


print(dbl_list.contains('C++'))
print(dbl_list.contains('C#'))


