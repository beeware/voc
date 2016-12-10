def test_function():
    try:
        obj = int('asdf')
        print('OK')
    except NameError:
        print("Got a NameError")
    except AttributeError as e:
        print("Got an AttributeError", e)
    print('Done.')
    
test_function()