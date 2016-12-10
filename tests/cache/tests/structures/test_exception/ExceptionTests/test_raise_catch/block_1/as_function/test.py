def test_function():
    try:
        raise KeyError("This is the name")
        print("No error")
    except KeyError:
        print("Got a Key Error")
    print('Done.')
    
test_function()