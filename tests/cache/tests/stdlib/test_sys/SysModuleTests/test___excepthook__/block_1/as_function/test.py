def test_function():
    import sys
    print(sys.__excepthook__())
    print('Done.')
    
test_function()