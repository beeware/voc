def test_function():
    x = [1, 2, 3, 4, 5]
    s = {v**2 for v in x}
    print(len(s))
    print(1 in s)
    print(4 in s)
    print(9 in s)
    print(16 in s)
    print(25 in s)
    print('Done.')
    
test_function()