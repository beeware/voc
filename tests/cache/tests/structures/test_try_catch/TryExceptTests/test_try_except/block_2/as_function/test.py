def test_function():
    try:
        obj.no_such_attribute
        print('OK')
    except:
        print("Got an error")
    print('Done.')
    
test_function()