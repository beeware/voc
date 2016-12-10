def test_function():
    try:
        print('>>> f = bin')
        print('>>> x = None')
        print('>>> f(x)')
        f = bin
        x = None
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()