message = "bonjour and welcome to Paris!"
 
print(message.upper())  # BONJOUR AND WELCOME TO PARIS!
# `message` is not changed
print(message)  # bonjour and welcome to Paris!
 
title_message = message.title() 
# `title_message` contains a new string with all words capitalized
print(title_message)  # Bonjour And Welcome To Paris!
 
print(message.replace("Paris", "Lyon"))  # bonjour and welcome to Lyon!
replaced_message = message.replace("o", "!", 2)
print(replaced_message)  # b!nj!ur and welcome to Paris!
 
# again, the source string is unchanged, only its copy is modified
print(message)  # bonjour and welcome to Paris!

# str.replace(old, new[, count]) replaces all occurrences of the old string with the new one. The count parameter is optional, and if specified, only the first count occurrences are replaced in the given string.
# str.upper() converts all characters of the string to the upper case.

# str.lower() converts all characters of the string to the lower case.

# str.title() converts the first character of each word to upper case.

# str.swapcase() converts upper case to lower case and vice versa.

# str.capitalize() changes the first character of the string to the title case and the rest to the lower case.
