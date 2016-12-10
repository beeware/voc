def test_function():
    try:
        print('>>> f = isinstance')
        print('>>> x = None')
        print('>>> f(x)')
        f = isinstance
        x = None
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()