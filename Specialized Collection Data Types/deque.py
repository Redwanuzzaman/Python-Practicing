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
