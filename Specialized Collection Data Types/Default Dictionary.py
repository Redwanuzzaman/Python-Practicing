# defaultdict()
from collections import  defaultdict

d = defaultdict(int)
d[1] = 'a'
d[2] = 'b'
print(d) # defaultdict(<class 'int'>, {1: 'a', 2: 'b'})
print(d[4]) # prints 0 insted of any error
