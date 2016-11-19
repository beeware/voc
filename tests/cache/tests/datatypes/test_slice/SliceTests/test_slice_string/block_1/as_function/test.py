def test_function():
    x = "0123456789a"
    print("x[:] = ", x[:])
    print("x[5:] = ", x[5:])
    print("x[:5] = ", x[:5])
    print("x[2:8] = ", x[2:8])
    
    print("x[::2] = ", x[::2])
    print("x[5::2] = ", x[5::2])
    print("x[:5:2] = ", x[:5:2])
    print("x[2:8:2] = ", x[2:8:2])
    
test_function()