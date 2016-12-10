def test_function():
    x = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print("x[:] = ", x[:])
    print("x[5:] = ", x[5:])
    print("x[:5] = ", x[:5])
    print("x[2:8] = ", x[2:8])
    
    print("x[::2] = ", x[::2])
    print("x[5::2] = ", x[5::2])
    print("x[:5:2] = ", x[:5:2])
    print("x[2:8:2] = ", x[2:8:2])
    
test_function()