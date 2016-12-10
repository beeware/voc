def test_function():
    x = None
    if x is None:
        print('1: is none')
    else:
        print('1: is not none')
    print('Done 1.')
    
    if x is not None:
        print('2: is not none')
    else:
        print('2: is none')
    print('Done 2.')
    
test_function()