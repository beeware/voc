def test_function():
    try:
        obj = 3
        print('OK')
    except:
        print("Got an error")
    else:
        print("Do else handling")
    finally:
        print("Do final cleanup")
    print('Done.')
    
test_function()