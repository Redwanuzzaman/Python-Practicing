def recursive_factorial(n):
   if n == 1 or n == 0:
       return 1
   else:
       return n*recursive_factorial(n-1)
 
 
numbers = map(int, input().split())
 
factorial_list = []
for number in numbers:
    factorial_list.append(recursive_factorial(number))
 
print(factorial_list, sep=', ')
