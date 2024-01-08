#minimizing collisions in hash ord by multiplying the ordinal numbers, but it has some collisions

def myhash(item):
    mult=1
    hv=0

    for ch in item:
        hv += mult*ord(ch)
        mult+=1
    return hv 

for item in ('hello world', 'world hello', 'gello xorld'):
    print(f'hash function of {item}: {myhash(item)}')

print("========================\n")

#open addressing for eliminating collisions
#linear probing, quadratic probing and double hashing

class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self):
        self.size = 256
        self.slots = [None for i in range(self.size)]
        self.count = 0
        self.MAXLOADFACTOR = 0.65 #maximum percentage of used slots for increasing the size of slots
    
    #just for internal use
    def _hash(self, key):
        hv = 0
        mult = 1
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv % self.size
    
    def put(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)
        while self.slots[h] != None:
            if self.slots[h].key == key:
                break
            h = (h + 1) % self.size
        
        if self.slots[h] == None:
            self.count += 1
            self.slots[h] = item
            self.check_growth()
    
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
    
    def get(self, key):
        h = self._hash(key)
        while self.slots[h]!=None:
            if self.slots[h].key == key:
                return self.slots[h].value
            h = (h+1)%self.size
        return None

    #implement hashtable as dictionary
    def __setitem__(self, key, value):
        self.put(key, value)
    
    def __getitem__(self, key):
        return self.get(key)

    #quadratic probing vs linear probing
    def get_quadratic(self, key):
        h = self._hash(key)
        j = 1
        while self.slots[h] != None:
            if self.slots[h].key == key:
                return self.slots[h].value
            h = (h+ j**2) % self.size
            j = j + 1
        return None
    
    def put_quadratic(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)
        j = 1
        while self.slots[h] != None:
            if self.slots[h].key == key:
                break
            h = (h + j*j) % self.size
            j = j+1
        if self.slots[h] == None:
            self.count += 1
        self.slots[h] = item
        self.check_growth()
    
    
ht = HashTable() 
ht.put("good", "eggs") 
ht.put("better", "ham") 
ht.put("best", "spam") 
ht.put("ad", "do not") 
ht.put("ga", "collide")
ht.put("awd", "do not") 
ht.put("add", "do not") 
ht.check_growth()

print("++++++++++++++++++")

ht = HashTable()
ht.put("good", "eggs")
ht.put("better", "ham")
ht.put("best", "spam")
ht.put("ad", "do not")
ht.put("ga", "collide")
for key in ("good", "better", "best", "worst", "ad", "ga"):
    v = ht.get(key)
    print(v)

#implement as dictionary
print("///////////")
ht = HashTable()
ht["good"] = "eggs"
ht["better"] = "ham"
ht["best"] = "spam"
ht["ad"] = "do not"
ht["ga"] = "collide"
for key in ("good", "better", "best", "worst", "ad", "ga"):
    v = ht[key]
    print(v)
print("The number of elements is: {}".format(ht.count))

#quadratic probing 
print("--------------------------")
ht = HashTable() 
ht.put_quadratic("good", "eggs") 
ht.put_quadratic("ad", "packt") 
ht.put_quadratic("ga", "books") 
 
v = ht.get_quadratic("ga") 
print(v)
