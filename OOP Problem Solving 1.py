# Problem Stastement
# John works at the university. He deals with the information about a lot of students and he decided to create a program that would help him with it. 

# He devised a system for creating an id for each student: first letter of the name, last name and then the birth year. For example, the id for John Smith (b. 1989) would look like JSmith1989.

# John needs help finishing the code for the id and then applying it to the students. Create an instance attribute id in the __init__ method, calculate it and then print its value for the student.

# The input format:

# Student information: the first line has the name, the second has the last name, and the third has the birth year.

# The output format:

# The id of the student.

# Sample Input 1:

# Daniel
S# mith
# 1993
# Sample Output 1:

# DSmith1993



class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = name[0] + last_name + str(birth_year)


name = input()
last_name = input()
birth_year = input()
student = Student(name, last_name, birth_year)
print(student.id)



