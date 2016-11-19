def test_function():
    try:
        obj = 3
        print('OK')
    finally:
        print("Do final cleanup")
    print('Done.')
    
test_function()