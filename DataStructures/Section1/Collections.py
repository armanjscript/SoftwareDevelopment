from collections import namedtuple, deque, OrderedDict, defaultdict, ChainMap, Counter, UserDict, UserList

#NamedTuple
Book = namedtuple('Book', ['name', 'ISBN', 'quantity'])
Book1 = Book('Hands on Data Structures', '9781788995573', '50')

print('Using index ISBN: '+ Book1[1])
print('Using key ISBN: '+Book1.ISBN)


#Double Ended Queue
s = deque()
print(s)
my_queue = deque([1, 2, 'Name'])
print(my_queue)

my_queue.append('age')
my_queue.appendleft('age')
print(my_queue)
my_queue.pop()
print(my_queue)

#Ordered dictionaries

od = OrderedDict({'my':1, 'name':2, 'is':3, 'Arman':4})
od['hello'] = 5
print(od)

#normal way to initialize dictionary

dd = defaultdict(int)
words = str.split('data python data data structure data python')
for word in words:
    dd[word] +=1
print(dd)

#ChainMap

dict1 = {'hello':1, 'world':2}
dict2 = {'python':3, 'c++':4}

chain = ChainMap(dict1, dict2)

print(chain)
print(list(chain.keys()))
print(list(chain.values()))
print(chain['hello'])
print(chain['world'])

#Counter

mynums = Counter([1, 1, 2, 3, 8, 6, 3])
print(mynums[1]) #counts the number of 1 in the list 
print(mynums[8])

# define a dictionary that doesnt allow to push elements in it (by UserDict)

class MyDict(UserDict):
    def push(self, key, value):
        raise RuntimeError('You are not allowed to push elements in dictionary')

d = MyDict({'ab':1, 'cd':2, 'ef':3 })
# d.push('gh', 4)

class MyList(UserList):
    def push(self, value):
        raise RuntimeError('Cannot insert in the list')
li = MyList([11, 12, 13])
li.push(2)

