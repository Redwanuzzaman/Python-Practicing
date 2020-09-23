# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.


try:
  print(x)
except:
  print("An exception occurred")
  
# output (An exception occurred)


# Print one message if the try block raises a NameError and another for other errors:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
 
 
# The finally block, if specified, will be executed regardless if the try block raises an error or not.

try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()
  
  
# The raise keyword is used to raise an exception.
# You can define what kind of error to raise, and the text to print to the user.

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
  
  
# CATCHING EXCEPTIONS

# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)

# output:
# The entry is a
# Oops! <class 'ValueError'> occurred.
# Next entry.
# 
# The entry is 0
# Oops! <class 'ZeroDivisionError'> occured.
# Next entry.
# 
# The entry is 2
# The reciprocal of 2 is 0.5# 


randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)

# output: SAME


except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
