# Join all items in a tuple into a string Here using a hash character as separator:

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)  # John#Peter#Vicky

# Another Example

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x) # nameTESTcountry
