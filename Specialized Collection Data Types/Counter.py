# Counter
from collections import Counter

a = [1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,5]
c = Counter(a)
print(c) # Counter({3: 7, 2: 5, 1: 3, 4: 3, 5: 1})
