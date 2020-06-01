class River:
    # list of all rivers
    all_rivers = []
    
    def __init__(self, name, length):
        self.name = name
        self.length = length
        # add current river to the list of all rivers
        River.all_rivers.append(self)
        
    def get_info(self):
        print("The length of the {0} is {1} km".format(self.name, self.length))
 
volga = River("Volga", 3530)
seine = River("Seine", 776)
nile = River("Nile", 6852)
 
# print all river names
for river in River.all_rivers:
    print(river.name)
# Output:
# Volga
# Seine
# Nile

volga.get_info()
# The length of the Volga is 3530 km
seine.get_info()
# The length of the Seine is 776 km
nile.get_info()
# The length of the Nile is 6852 km

# 2 ways of calling a method
# self.method()
volga.get_info()
# The length of the Volga is 3530 km
 
# class.method(self)
River.get_info(volga)
# The length of the Volga is 3530 km
