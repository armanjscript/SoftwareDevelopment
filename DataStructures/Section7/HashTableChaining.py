class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None

    def append(self, key, value):
        new_node = Node(key, value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def traverse(self, key):
        current = self.head
        while current:
            print("\"", current.key, "--", current.value, "\"")
            current = current.next
    
    def search(self, key):
        current = self.head
        while current:
            if current.key == key:
                print("\"Record found:", current.key, "-", current.value, "\"")
                return True
            current = current.next
        return False
    

class HashTableChaining:
    def __init__(self):
        self.size = 6
        self.slots = [None for i in range(self.size)]
        for x in range(self.size) :
            self.slots[x] = SinglyLinkedList()
    
    def _hash(self, key):
        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv % self.size
    
    def put(self, key, value):
        node = Node(key, value)        
        h = self._hash(key) 
        self.slots[h].append(key, value)
    
    def get(self, key):
        h = self._hash(key)
        v = self.slots[h].search(key)

    def printHashTable(self) :
        print("Hash table is :- \n")
        print("Index \t\tValues\n")
        for x in range(self.size) :
            print(x,end="\t\n")
            self.slots[x].traverse()
    

ht = HashTableChaining() 
ht.put("good", "eggs") 
ht.put("better", "ham") 
ht.put("best", "spam") 
ht.put("ad", "do not") 
ht.put("ga", "collide") 
ht.put("awd", "do not") 
        
ht.printHashTable()