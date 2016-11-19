def test_function():
    try:
        obj = 3
        print('OK')
    except:
        print("Got an error")
    else:
        print("Do else handling")
    print('Done.')
    
test_function()