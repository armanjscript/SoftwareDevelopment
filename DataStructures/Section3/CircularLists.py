class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularList:

    def __init__(self):

        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, data):

        new_node = Node(data)
        
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.tail
        self.size+=1
    
    def iter(self):

        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val
            if current == self.head:
                break
    
    def remove(self, data):

        current = self.head
        prev = self.head
        Flag = False
        while prev == current or prev!=self.tail:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    self.tail.next = self.head
                    Flag = True
                elif current == self.tail:
                    self.tail = prev
                    prev.next = self.head
                    Flag = True
                else:
                    prev.next = current.next
                    Flag = True
                self.size-=1
                return
            prev = current
            current = current.next
        if Flag is False:
            print('No item here')
            return




        

circular = CircularList()
circular.append('Python')
circular.append('C++')
circular.append('JavaScript')

for item in circular.iter():
    print(item)

circular.append('C#')
circular.append('Java')

circular.remove('C#')



print("===============")
for item in circular.iter():
    print(item)