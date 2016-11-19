def test_function():
    try:
        obj = 3
        print('OK')
    except NameError as e:
        print("Got a NameError", e)
    print('Done.')
    
test_function()