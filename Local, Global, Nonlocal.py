def outer():
    x = "local"

    def inner():
        global x
        x = "global"
        print("inner: ", x)

    inner()  # global
    print("outer: ", x)  # local
    
    def inner2():
        nonlocal x
        x = "nonlocal"
        print("inner 2: ", x)
        
    inner2()  # nonlocal
    
    print("outer: ", x)  # nonlocal

outer()
print("outside of method:", x)  # global
