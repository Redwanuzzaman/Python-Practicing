class Sun:
    n = 0
 
    def __new__(cls):
        if cls.n == 0:
            instance = object.__new__(cls)
            cls.n += 1
            return instance
            
            
sun1 = Sun()
sun2 = Sun()
 
print(sun1)  # <__main__.Sun object at 0x1106884a8>
print(sun2)  # None
