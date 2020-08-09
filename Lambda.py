x = lambda a, b, c : a + b + c
print(x(5, 6, 2))  # 13


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))  # 22
print(mytripler(11))  # 33
