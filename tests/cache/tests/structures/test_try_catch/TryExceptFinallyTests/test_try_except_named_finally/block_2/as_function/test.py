def test_function():
    try:
        obj.no_such_attribute
        print('OK')
    except NameError as e:
        print("Got a NameError", e)
    finally:
        print("Do final cleanup")
    print('Done.')
    
test_function()