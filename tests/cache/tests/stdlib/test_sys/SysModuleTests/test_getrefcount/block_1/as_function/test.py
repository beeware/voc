def test_function():
    import sys
    print(sys.getrefcount())
    print('Done.')
    
test_function()