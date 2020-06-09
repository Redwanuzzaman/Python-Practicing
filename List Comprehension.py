# work with a list from this variable
numbers = [int(n) for n in input()]

# change the next two lines
less_than_5 = [x for x in numbers if x < 5]
greater_than_5 = [x for x in numbers if x > 5]

# printing your results
print(less_than_5)
print(greater_than_5)



# Write a program that takes a list with words, creates a new list of words that start with the letter "a" in the first list, and prints it.

# work with the preset variable `words`
ans = [x for x in words if x.startswith('a') or x.startswith('A')]
print(ans)
