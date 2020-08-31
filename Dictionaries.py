# Nested Dictionaries
employee_details = {'Employee': {'Redwan' : {'ID': '001', 'Dept': 'CSE'}, 'Saym': {"ID": '002', 'Dept': 'SCI'}}}
print(employee_details)

my_dict = {'Sayem': 1, 'Shagor': 2, 'Roktim': 3}
print(my_dict)
print(my_dict['Roktim']) # 3
print(my_dict.get('Sayem')) # 1
print(my_dict.keys()) # ['Sayem', 'Shagor', 'Roktim']
print(my_dict.values()) # [1, 2, 3]

for x in my_dict.values():
    print(x)  # print values of my_dict

for x,y in my_dict.items():
    print(x, y) # print both keys and values

# Updating
my_dict['Shagor'] = 13
print(my_dict)

# Removing
my_dict.pop('Shagor')
print(my_dict) # {'Sayem': 1, 'Roktim': 3}
my_dict.popitem()
print(my_dict) # {'Sayem': 1}

# Looping Through Dictionaries
counts = dict()
for line in input_file:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

 
# Updating values in Dict

dictionary[key] = dictionary.get(key, 0) + 1
