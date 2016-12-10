def test_function():
    x = {1: 2}
    print(x.get([]))
    print(x.get([], 1))
    
test_function()