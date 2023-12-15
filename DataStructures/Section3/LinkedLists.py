# Node Class

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

n1 = Node("Python")
n2 = Node("C++")
n3 = Node("Java")


n1.next = n2
n2.next = n3

current = n1

while current:
    print(current.data)
    current = current.next

# Singly LinkedList

class SinglyLinkedList:
    
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
            self.size +=1
        else:
            self.head = node
            self.tail = node
            self.size +=1
    
    def append_loc(self, data, index):
        
        current = self.head
        prev = self.head
        counter = 0
        node = Node(data)

        while current:
            if index == 0:
                node.next = current
                self.head = node
                self.size +=1
            elif counter == index:
                node.next = current
                prev.next = node
                self.size+=1
                return
            counter +=1
            prev = current
            current = current.next
        if counter < index:
            print("The list has less number of elements")

    def iter(self):
        if self.size == 0:
            print('No items here')
        else:
            current = self.head
            while current:
                val = current.data
                current = current.next
                yield val
    
    def search(self, data):
        for node in self.iter():
            if node == data:
                return True
        return False
    def length(self):
        return self.size
    
    def delete_first(self):
        current = self.head
        if self.head is None:
            print("No items here")
        else:
            self.head = current.next
            self.size -=1
    
    def delete_last(self):
        current = self.head
        prev = self.head

        while current:
            if current.next is None:
                prev.next = current.next
                self.size -=1
            prev = current
            current = current.next
    
    def delete(self, data):

        current = self.head
        prev = self.head

        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                self.size -=1
                return
            prev = current
            current = current.next
    
    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0

print("++++++++++++++++++")
words = SinglyLinkedList()
words.append('Python')
words.append('Java')
words.append('C++')
words.append('C#')
words.append_loc('Javascript', 3) #append item to specific location in the linkedlist
words.delete_first()
words.delete_last()
words.delete('Java')

for word in words.iter():
    print(word)

print(words.search('Python'))
print(words.length())


words.clear()

for word in words.iter():
    print(word)