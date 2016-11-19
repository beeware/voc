def test_function():
    try:
        obj = 3
        print('OK')
    except NameError:
        print("Got a NameError")
    except AttributeError:
        print("Got an AttributeError")
    print('Done.')
    
test_function()