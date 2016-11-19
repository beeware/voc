def test_function():
    try:
        obj = int('asdf')
        print('OK')
    finally:
        print("Do final cleanup")
    print('Done.')
    
test_function()