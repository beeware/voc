def test_function():
    try:
        obj = int('asdf')
        print('OK')
    except NameError:
        print("Got a NameError")
    except AttributeError:
        print("Got an AttributeError")
    print('Done.')
    
test_function()