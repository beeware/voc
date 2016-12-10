def test_function():
    try:
        obj = int('asdf')
        print('OK')
    except NameError as e:
        print("Got a NameError", e)
    except AttributeError as e:
        print("Got an AttributeError", e)
    print('Done.')
    
test_function()