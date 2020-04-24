# namedtuple
from collections import  namedtuple

a = namedtuple('students', 'name, department')
s = a('redwan', 'cse')
print(s)

s = a._make(['sayem', 'doctor'])
print(s)

# deque
from collections import deque

a = ['a', 'b', 'c', 'd']
d = deque(a)
print(d) #deque(['a', 'b', 'c', 'd'])
d.append('e')
print(d) # deque(['a', 'b', 'c', 'd', 'e'])
d.appendleft('z')
print(d) # deque(['z', 'a', 'b', 'c', 'd', 'e'])
d.popleft()
d.popleft()
print(d) # deque(['b', 'c', 'd', 'e'])

# Chainmap
from collections import ChainMap

a = {1: 'a', 2: 'b'}
b = {3: 'c', 4: 'd'}

res = ChainMap(a, b)

print(res) # ChainMap({1: 'a', 2: 'b'}, {3: 'c', 4: 'd'})

# Counter
from collections import Counter

a = [1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,5]
c = Counter(a)
print(c) # Counter({3: 7, 2: 5, 1: 3, 4: 3, 5: 1})
print(list(c.elements())) # [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5]

sub = {2:1, 5:1}
c.subtract(sub)
print(c.most_common()) # [(3, 7), (2, 4), (1, 3), (4, 3), (5, 0)]

# Ordered Dictionary
from collections import OrderedDict
d = OrderedDict()
d[1] = 'a'
d[2] = 'b'
d[3] = 'c'
d[4] = 'd'
d[5] = 'e'
print(d) # OrderedDict([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')])
d[1] = 'm'
print(d) # OrderedDict([(1, 'm'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')])

# defaultdict()
from collections import  defaultdict

d = defaultdict(int)
d[1] = 'a'
d[2] = 'b'
print(d) # defaultdict(<class 'int'>, {1: 'a', 2: 'b'})
print(d[4]) # prints 0 instead of any error
