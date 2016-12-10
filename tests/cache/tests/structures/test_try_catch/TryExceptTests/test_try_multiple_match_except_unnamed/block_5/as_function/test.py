def test_function():
    try:
        obj.no_such_attribute
        print('OK')
    except AttributeError:
        print("Got an AttributeError")
    except (TypeError, NameError):
        print("Got a TypeError or NameError")
    print('Done.')
    
test_function()