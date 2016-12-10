def test_function():
    try:
        obj.no_such_attribute
        print('OK')
    except AttributeError:
        print("Got an AttributeError")
    except NameError:
        print("Got a NameError")
    print('Done.')
    
test_function()