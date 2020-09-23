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
  
  
