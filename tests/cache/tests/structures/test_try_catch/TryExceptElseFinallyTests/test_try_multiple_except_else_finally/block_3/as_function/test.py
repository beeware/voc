def test_function():
    try:
        obj = int('asdf')
        print('OK')
    except NameError:
        print("Got a NameError")
    except AttributeError as e:
        print("Got an AttributeError", e)
    else:
        print("Do else handling")
    finally:
        print("Do final cleanup")
    print('Done.')
    
test_function()