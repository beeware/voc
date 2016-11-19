def test_function():
    def second(s):
        return s[1]
    
    x = ['abc', 'bza', 'cda', 'daa']
    x.sort(key=second, reverse=True)
    print(x)
    
test_function()