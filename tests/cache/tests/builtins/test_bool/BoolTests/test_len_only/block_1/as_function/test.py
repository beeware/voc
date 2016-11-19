def test_function():
    class LenButNoBool:
        def __init__(self, val):
            self.val = val
    
        def __len__(self):
            return self.val
    
    print(bool(LenButNoBool(0)))
    print(bool(LenButNoBool(1)))
    
test_function()