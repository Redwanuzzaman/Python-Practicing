from collections import Counter 
  
# Create a list 
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red'] 
col_count = Counter(z) 
print(col_count) # Counter({'blue': 3, 'red': 2, 'yellow': 1})

  
col = ['blue','red','yellow','green'] 
  
# Here green is not in col_count  
# so count of green will be zero 
for color in col: 
    print (color, col_count[color]) 
    
"""
blue 3
red 2
yellow 1
green 0
"""
