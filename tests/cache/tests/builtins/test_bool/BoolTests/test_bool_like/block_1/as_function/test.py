def test_function():
    class BoolLike:
        def __init__(self, val):
            self.val = val
    
        def __bool__(self):
            return self.val == 1
    
    print(bool(BoolLike(0)))
    print(bool(BoolLike(1)))
    
test_function()