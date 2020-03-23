string_array = ["Hello", "Jello", "Mello", "Tello"]
int_array = [10, 20, 30, 40, 50, 60, 70]
id = [4, 3, 2, 1]
val = string_array[1]
print(int_array[3:]) # [40, 50, 60, 70]
print(int_array[0:3]) # (prints from index 0 to 2) [10, 20, 30]
print(int_array[-1]) # prints last indexed value (70)
print(int_array[-3]) # prints third last value of the array

print(string_array)
print(int_array)

# LIST EXTEND FUNCTION
string_array.extend(id) # id array will add with string_array
print("Extended String Array:", end = " ") # printing without newline
print(string_array)

# LIST APPEND FUNCTION
print(id)
id.append(5)
print("After Append 5 in id:", end = " ")
print(id)

# LIST INSERT FUNCTION
print(id)
id.insert(2, 4) # insert 4 at index 2
print("After inserting 39 at idx 2:", end = " ")
print(id)

# LIST REMOVE FUNCTION
print(string_array)
string_array.remove("Mello")
print("String Array after removing \'Mello\'", end = " ")
print(string_array)

# FINDING AN INDEX OF A VALUE IN LIST
print(id)
a = id.index(1)
print("Index of 1 is: ", a)   # id = {4, 3, 4, 2, 1 , 5} So, the index of 1 is 4 

# LIST POP FUNCTION
id.pop() # Pops the last element of the array
print("After Poping:", end = " ")
print(id)

# LIST COUNT FUNCTION
print("Number of 4s in id:", end = " ")
print(id.count(4))

# LIST SORT FUNCTION
id.sort() # sort in ascending order
print("After Sorting:", end = " ")
print(id)

# LIST REVERSE FUNCTION
id.reverse();
print("After Reversing:", end = " ")
print(id)

# LIST COPY FUNCTION
id2 = id.copy(); # copies id array as it is at id2
print("id2 =", end = " ")
print(id2)

# LIST LENGTH CHECKING FUNCTION
print(len(id2)) # prints the number of elements present in id2 array

# LIST CLEAR FUNCTION
id2.clear();
print("After Clearing id2 becomes:", end = " ")
print(id2)
