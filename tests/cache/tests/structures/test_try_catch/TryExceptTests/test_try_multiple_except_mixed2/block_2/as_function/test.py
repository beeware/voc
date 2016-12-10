def test_function():
    try:
        obj.no_such_attribute
        print('OK')
    except NameError as e:
        print("Got a NameError", e)
    except AttributeError:
        print("Got an AttributeError")
    print('Done.')
    
test_function()