def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner: ", x)

    inner()  # inner: nonlocal
    print("outer:", x)  # outer: nonlocal


outer()
print(x)  # error
