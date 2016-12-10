def test_function():
    class FileLikeObject:
        def __init__(self):
            self.buffer = ''
    
        def write(self, content):
            self.buffer = self.buffer + (content * 2)
    
    out = FileLikeObject()
    
    print('hello', 'world', file=out)
    print('goodbye', 'world', file=out)
    print()
    
test_function()