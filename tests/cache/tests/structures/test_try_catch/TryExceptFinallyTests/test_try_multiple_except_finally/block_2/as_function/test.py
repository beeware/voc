def test_function():
    try:
        obj.no_such_attribute
        print('OK')
    except NameError:
        print("Got a NameError")
    except AttributeError as e:
        print("Got an AttributeError", e)
    finally:
        print("Do final cleanup")
    print('Done.')
    
test_function()