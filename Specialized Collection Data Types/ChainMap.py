# Chainmap
from collections import ChainMap

a = {1: 'a', 2: 'b'}
b = {3: 'c', 4: 'd'}

res = ChainMap(a, b)

print(res) # ChainMap({1: 'a', 2: 'b'}, {3: 'c', 4: 'd'})
