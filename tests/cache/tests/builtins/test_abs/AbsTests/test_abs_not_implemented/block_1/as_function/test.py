def test_function():
    class NotAbsLike:
        pass
    x = NotAbsLike()
    print(abs(x))
    
test_function()