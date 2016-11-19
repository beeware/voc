def test_function():
    try:
        raise KeyError("This is the name")
        print("No error")
    except:
        print("Got error")
        raise
    print('Done.')
    
test_function()