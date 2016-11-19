def test_function():
    try:
        obj = 3
        print('OK')
    except NameError:
        print("Got an error")
    print('Done.')
    
test_function()