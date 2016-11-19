def test_function():
    try:
        obj = int('asdf')
        print('OK')
    except (NameError, TypeError):
        print("Got a NameError or TypeError")
    except AttributeError:
        print("Got an AttributeError")
    print('Done.')
    
test_function()