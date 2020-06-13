import re

string = "My 2 favorite numbers are 13 and 18"

y = re.findall('[0-9]+', string)  # extract digits
print(y)
