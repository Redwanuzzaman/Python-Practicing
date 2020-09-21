# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The frozen set is:', fSet)  # The frozen set is: frozenset({'a', 'o', 'u', 'i', 'e'})

print('The empty frozen set is:', frozenset())  # The empty frozen set is: frozenset()

# frozensets are immutable
fSet.add('v')  # Traceback (most recent call last):


# random dictionary
person = {"name": "John", "age": 23, "sex": "male"}

fSet = frozenset(person)
print('The frozen set is:', fSet)  # The frozen set is: frozenset({'name', 'sex', 'age'})


# Frozensets Operations

# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# copying a frozenset
C = A.copy()  # Output: frozenset({1, 2, 3, 4})
print(C)  # frozenset({1, 2, 3, 4})

# union
print(A.union(B))  # Output: frozenset({1, 2, 3, 4, 5, 6})

# intersection
print(A.intersection(B))  # Output: frozenset({3, 4})

# difference
print(A.difference(B))  # Output: frozenset({1, 2})

# symmetric_difference
print(A.symmetric_difference(B))  # Output: frozenset({1, 2, 5, 6})


# Similarly, other set methods like isdisjoint, issubset, and issuperset are also available.
# Frozensets
# initialize A, B and C

A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = frozenset([5, 6])

# isdisjoint() method
print(A.isdisjoint(C))  # Output: True

# issubset() method
print(C.issubset(B))  # Output: True

# issuperset() method
print(B.issuperset(C))  # Output: True
