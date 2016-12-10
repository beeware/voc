def test_function():
    try:
        print('>>> x = NotImplemented')
        print('>>> not x')
        x = NotImplemented
        print(not x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()