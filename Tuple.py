# Tuples basic functionality is as same as a LIST.
# The main diiference is TUPLE is immutable. Which means it can't be modified or changed.
# Once a tuple is created, it's created forever.
# Tuples initialized with parenthesis "()"


# Initializing a TUPLE
coordinates = (7,5)
print(coordinates)
print(coordinates[0]) # prints 7 as it's in index 0

# LIST of TUPLEs
name_id = [("Jodu", 12), ("Kodu", 17), ("Ludu", 23)]
print(name_id) # prints the list of tuples
print(name_id[0]) # prints ('Jodu', 12)


TUPLE: 

A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.

Creating a Tuple
A tuple is created by placing all the items (elements) inside parentheses (), separated by commas. The parentheses are optional, however, it is a good practice to use them.
A tuple can have any number of items and they may be of different types (integer, float, list, string, etc.).
# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)
Output
()
(1, 2, 3)
(1, 'Hello', 3.4)
('mouse', [8, 4, 6], (1, 2, 3))
A tuple can also be created without using parentheses. This is known as tuple packing.
my_tuple = 3, 4.6, "dog"
print(my_tuple)

# tuple unpacking is also possible
a, b, c = my_tuple

print(a)      # 3
print(b)      # 4.6
print(c)      # dog
Output
(3, 4.6, 'dog')
3
4.6
dog
Access Tuple Elements
There are various ways in which we can access the elements of a tuple.
1. Indexing
We can use the index operator [] to access an item in a tuple, where the index starts from 0.
So, a tuple having 6 elements will have indices from 0 to 5. Trying to access an index outside of the tuple index range(6,7,... in this example) will raise an IndexError.
The index must be an integer, so we cannot use float or other types. This will result in TypeError.
Likewise, nested tuples are accessed using nested indexing, as shown in the example below.
# Accessing tuple elements using indexing
my_tuple = ('p','e','r','m','i','t')

print(my_tuple[0])   # 'p' 
print(my_tuple[5])   # 't'

# IndexError: list index out of range
# print(my_tuple[6])

# Index must be an integer
# TypeError: list indices must be integers, not float
# my_tuple[2.0]

# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
print(n_tuple[0][3])       # 's'
print(n_tuple[1][1])       # 4
Output
p
t
s
4
Changing a Tuple
Unlike lists, tuples are immutable.
This means that elements of a tuple cannot be changed once they have been assigned. But, if the element is itself a mutable data type like list, its nested items can be changed.
We can also assign a tuple to different values (reassignment).
# Changing tuple values
my_tuple = (4, 2, 3, [6, 5])


# TypeError: 'tuple' object does not support item assignment
# my_tuple[1] = 9

# However, item of mutable element can be changed
my_tuple[3][0] = 9    # Output: (4, 2, 3, [9, 5])
print(my_tuple)

# Tuples can be reassigned
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple)
# Concatenation
# Output: (1, 2, 3, 4, 5, 6)
print((1, 2, 3) + (4, 5, 6))

# Repeat
# Output: ('Repeat', 'Repeat', 'Repeat')
print(("Repeat",) * 3)
Deleting a Tuple
As discussed above, we cannot change the elements in a tuple. It means that we cannot delete or remove items from a tuple.
Deleting a tuple entirely, however, is possible using the keyword del.
# Deleting tuples
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# can't delete items
# TypeError: 'tuple' object doesn't support item deletion
# del my_tuple[3]

# Can delete an entire tuple
del my_tuple


Tuple Methods
Methods that add items or remove items are not available with tuple. Only the following two methods are available.
Some examples of Python tuple methods:
my_tuple = ('a', 'p', 'p', 'l', 'e',)

print(my_tuple.count('p'))  # Output: 2
print(my_tuple.index('l'))  # Output: 3
Output
2
3

Other Tuple Operations
1. Tuple Membership Test
We can test if an item exists in a tuple or not, using the keyword in.
# Membership test in tuple
my_tuple = ('a', 'p', 'p', 'l', 'e',)

# In operation
print('a' in my_tuple)
print('b' in my_tuple)

# Not in operation
print('g' not in my_tuple)
Output
True
False
True

2. Iterating Through a Tuple
We can use a for loop to iterate through each item in a tuple.
# Using a for loop to iterate through a tuple
for name in ('John', 'Kate'):
    print("Hello", name)
Output
Hello John
Hello Kate

Advantages of Tuple over List
Since tuples are quite similar to lists, both of them are used in similar situations. However, there are certain advantages of implementing a tuple over a list. Below listed are some of the main advantages:
We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
Since tuples are immutable, iterating through a tuple is faster than with list. So there is a slight performance boost.
Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.
