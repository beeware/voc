def test_function():
    class NoLenNoBool:
        def __init__(self, val):
            self.val = val
    
    print(bool(NoLenNoBool(0)))
    print(bool(NoLenNoBool(1)))
    print(bool(NoLenNoBool(42)))
    print(bool(NoLenNoBool(-2)))
    
test_function()