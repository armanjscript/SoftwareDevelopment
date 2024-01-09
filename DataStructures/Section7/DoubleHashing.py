class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class DoubleHashTable:
    
    def __init__(self):
        self.size = 256
        self.slots = [None for i in range(self.size)]
        self.count = 0
        self.MAXLOADFACTOR = 0.65
        self.prime_num = 5
    
    #just for internal use (main hash function)
    def _hash(self, key):
        hv = 0
        mult = 1
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv % self.size
    
    #secondary hash function
    def h2(self, key):
        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv
    
    def put(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)
        j=1

        while self.slots[h]!= None:
            if self.slots[h].key == key:
                break
            h = (h + j * (self.prime_num - (self.h2(key) % self.prime_num))) % self.size
            j = j+1
        
        if self.slots[h] == None:
            self.count += 1
        self.slots[h] = item
        self.check_growth()

    def get(self, key):
        h = self._hash(key)
        j = 1
        while self.slots[h] != None:
            if self.slots[h].key == key:
                return self.slots[h].value
            h = (h + j * (self.prime_num - (self.h2(key) % self.prime_num))) % self.size
            j = j + 1
        return None
    
    def check_growth(self):
        loadfactor = self.count / self.size
        if loadfactor > self.MAXLOADFACTOR:
            print("Load factor before growing the hash table", self.count / self.size )
            self.growth()
            print("Load factor after growing the hash table", self.count / self.size )
    
    def growth(self):
        new_hash_table = HashTable()
        new_hash_table.size = 2 * self.size
        new_hash_table.slots = [None for i in range(new_hash_table.size)]

        for i in range(self.size):
            if self.slots[i] != None:
                new_hash_table.put(self.slots[i].key, self.slots[i].value)
        
        self.size = new_hash_table.size
        self.slots = new_hash_table.slots



ht = DoubleHashTable() 
ht.put("good", "eggs") 
ht.put("better", "spam") 
ht.put("best", "cool") 
ht.put("ad", "donot") 
ht.put("ga", "collide") 
ht.put("awd", "hello") 
ht.put("addition", "ok")

for key in ("good", "better", "best", "worst", "ad", "ga"): 
        v = ht.get(key) 
        print(v) 
print("The number of elements is: {}".format(ht.count))