def test_function():
    try:
        obj.no_such_attribute
        print('OK')
    except (TypeError, NameError):
        print("Got a TypeError or NameError")
    except AttributeError:
        print("Got an AttributeError")
    print('Done.')
    
test_function()