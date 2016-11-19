def test_function():
    from example import *
    
    try:
        raise MyException("This is the exception")
    except MyException:
        print("Got a custom exception")
    print('Done.')
    
test_function()