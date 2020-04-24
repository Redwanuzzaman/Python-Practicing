# Counter
from collections import Counter

a = [1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,5]
c = Counter(a)
print(c) # Counter({3: 7, 2: 5, 1: 3, 4: 3, 5: 1})
print(list(c.elements())) # [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5]

sub = {2:1, 5:1}
c.subtract(sub)
print(c.most_common()) # [(3, 7), (2, 4), (1, 3), (4, 3), (5, 0)]
