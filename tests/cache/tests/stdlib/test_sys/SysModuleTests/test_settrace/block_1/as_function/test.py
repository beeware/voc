def test_function():
    import sys
    print(sys.settrace())
    print('Done.')
    
test_function()