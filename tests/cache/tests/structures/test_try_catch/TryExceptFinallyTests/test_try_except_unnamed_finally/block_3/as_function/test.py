def test_function():
    try:
        obj = int('asdf')
        print('OK')
    except NameError:
        print("Got an error")
    finally:
        print("Do final cleanup")
    print('Done.')
    
test_function()