def test_function():
    class IntLike:
        def __init__(self, val):
            self.val = val
        def __int__(self):
            return self.val
    
    x = IntLike(5)
    print(bin(x))
    
test_function()