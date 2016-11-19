def test_function():
    try:
        obj.no_such_attribute
        print('OK')
    except NameError:
        print("Got a NameError")
    except AttributeError:
        print("Got an AttributeError")
    print('Done.')
    
test_function()