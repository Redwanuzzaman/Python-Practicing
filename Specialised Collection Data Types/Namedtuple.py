# namedtuple

from collections import  namedtuple

a = namedtuple('students', 'name, department')
s = a('redwan', 'cse')
print(s)

s = a._make(['sayem', 'doctor'])
print(s)
