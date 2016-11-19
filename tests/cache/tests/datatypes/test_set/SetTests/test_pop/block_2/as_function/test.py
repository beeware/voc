def test_function():
    x = {'a'}
    print(len(x) == 1)
    x.pop()
    print(len(x) == set())
    
test_function()