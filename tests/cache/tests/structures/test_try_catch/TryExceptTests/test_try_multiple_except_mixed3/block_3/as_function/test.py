def test_function():
    try:
        obj = int('asdf')
        print('OK')
    except NameError as e:
        print("Got a NameError", e)
    except AttributeError:
        print("Got an AttributeError")
    except:
        print("Got an anonymous error")
    print('Done.')
    
test_function()