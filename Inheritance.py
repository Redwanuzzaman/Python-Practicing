class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


class Employee(Person):
    def __init__(self, fname, lname, company_name):
        super().__init__(fname, lname)
        self.company = company_name

    def welcome(self):
        print("Hello {} {}\nWelcome to {}".format(self.firstname, self.lastname, self.company))


emp1 = Employee("Md", "Redwanuzzaman", "Divine IT Ltd")
emp1.welcome()

# output
"""
Hello Md Redwanuzzaman
Welcome to Divine IT Ltd
"""
