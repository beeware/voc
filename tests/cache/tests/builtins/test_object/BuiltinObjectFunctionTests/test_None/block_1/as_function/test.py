def test_function():
    try:
        print('>>> f = object')
        print('>>> x = None')
        print('>>> f(x)')
        f = object
        x = None
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()