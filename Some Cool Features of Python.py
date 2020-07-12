# Reverse Indexing : you can easily access last element with “-1” index without knowing the length. 
# Likewise reversing the string in Python, it’s one liner
"HELLO WORLD"[::-1]
'DLROW OLLEH'


# Free style typing: Sometimes you feel like you are just typing,
if 'GREEN' in ['RED','YELLOW','GREEN']:
    print"GO"
    
    
# List comprehension (similarly for other iterable tuples, dicts): 
# It makes code shorter but sometimes code loses the readability. 
# Sometimes I don’t understand my own code after a month. :)
# For example, you can write this
l=[]
for item in range(0,11):    
	l.append(item)
print l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# as one liner,

[item for item in range(0,11)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Also, you can apply if condition within list comprehension. Suppose we want cube of odd numbers in the range 0 to 10,

[item**3 for item in range(0,11) if item%2 != 0]
[1, 27, 125, 343, 729]

# Further, you can apply if else condition both,

[item**3 if item%2 != 0 else 'EVEN' for item in range(0,11)
['EVEN', 1, 'EVEN', 27, 'EVEN', 125, 'EVEN', 343, 'EVEN', 729, 'EVEN']

# Another example of list comprehension would be matrix multiplication with nested for loops. Generally, we would do something like this:

list1 = [1,2,3]
list2 = [4,5,6]
l=[] 
for item in list1:    
	for num in list2:        
		l.append(item*num)        
print l
[4, 5, 6, 8, 10, 12, 12, 15, 18]

# Now you can do above with this one liner list comprehension:

[item*num for item in list1 for num in list2]
[4, 5, 6, 8, 10, 12, 12, 15, 18]


# Dynamic typing: You can re-assign variable different values and type will be dynamically changed. Like below string to float.
my_var = "Hello"
my_var = 10.0


# String multiplication: You can multiply string “a” with any integer like,
'a'*10
'aaaaaaaaaa'


# Chain comparison: For example if you want to check if a number is between 100 to 1000
num = 200
if 100 < num < 1000:
    print True
    
    
# Iterable: You can iterate through any dict, list, string, tuple or any other iterable object.


# Range generator: Instead of storing the list in memory you can use generators, for instead, range which can hold any list of integers.
range(0,100)


# Pass: Leave the code block blank and come back whenever you want to write the block again.


# f-string in Python 3


# Extra else condition with while: I usually use it to check if while condition actually met or not.
X = False
while X:
    print"True"
else:
    print"False"
    
    
# for loop: Unlike C,C++ you don’t need to worry about initializing the variable and incrementing it. 
# Python made this so simple,
for letter in 'PYTHON':
    print letter
