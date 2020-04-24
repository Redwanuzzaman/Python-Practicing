# OrderedDict()
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
