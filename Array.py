import array as arr

a = arr.array('i', [1,2,3,4,5]) # i means array of integers
print(a)
print(a[2])
size = len(a)
print(size) # 5

b = arr.array('d', [1.2, 2.3, 3.5]) # d means double

# inserting in an array
a.append(10)
print(a) # appends at the end

a.extend([12, 15, 18])
print(a) # array('i', [1, 2, 3, 4, 5, 10, 12, 15, 18])

a.insert(3, 100) # inserts 100 at position 3
print(a)  # array('i', [1, 2, 3, 100, 4, 5, 10, 12, 15, 18])

# Removing Elements from array
print(a.pop()) # pops 18
print(a.pop(2)) # pops 3rd element which is 3
print(a) # array('i', [1, 2, 100, 4, 5, 10, 12, 15])

print(a.pop(-1)) # pops the last index value 15
a.remove(4)
print(a) # array('i', [1, 2, 100, 5, 10, 12])

# Array Concatenation
# data type must be same

a = arr.array('i', [1,2,3,4,5])
b = arr.array('i', [6,7,8,9,10])
c = arr.array('i')
c = a + b
print(c) # array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Slicing an array
print(c[0 : 3]) # [1, 2, 3]

print(c[0 : -2]) # array('i', [1, 2, 3, 4, 5, 6, 7, 8])

# Reversing an array
# Not changed the original array. Memory inefficient. Not recommended

print(c[::-1]) # array('i', [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

print(c) # array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Looping through an array

for x in c:
    print(x, end = " ")
print("") # 1 2 3 4 5 6 7 8 9 10

x = 0
while x < 5:
    print(c[x], end = " ") # 1 2 3 4 5

    x = x + 1
