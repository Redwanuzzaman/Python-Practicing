ZIP: 

Men = ['Romeo','Forhad','Majnu','Shajahan'] 
Women = ['Juliet','Siri','Laily','Momtaj'] 

for couple in zip(Men,Women): 
print(couple)

# Output
('Romeo', 'Juliet')
('Forhad', 'Siri')
('Majnu', 'Laily')
('Shajahan', 'Momtaj')
-----------------------------------------------

names = ('Richard','Danesh','Gylfoyl','Jarad','Erlick') 
positions = ('CEO','Software Eng','Tester','Legal Adviser','Sales Executive') 
salaries = (10000,8000,8000,5000,6000) 

for name,position,salary in zip(names,positions,salaries): 
print(f"{name} is the '{position}' and he is paid {salary}$ per week")


# output
Richard is the 'CEO' and he is paid 10000$ per week 
Danesh is the 'Software Eng' and he is paid 8000$ per week 
Gylfoyl is the 'Tester' and he is paid 8000$ per week 
Jarad is the 'Legal Adviser' and he is paid 5000$ per week 
Erlick is the 'Sales Executive' and he is paid 6000$ per week
