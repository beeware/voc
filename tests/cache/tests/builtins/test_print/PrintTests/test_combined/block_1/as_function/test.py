def test_function():
    class FileLikeObject:
        def __init__(self):
            self.buffer = ''
    
        def write(self, content):
            self.buffer = self.buffer + (content * 2)
    
        def flush(self):
            self.buffer = self.buffer + '<<<'
    
    out = FileLikeObject()
    
    print('hello', 'world', sep='*', end='-', file=out, flush=True)
    print('goodbye', 'world', file=out, sep='-', end='*')
    print()
    
test_function()