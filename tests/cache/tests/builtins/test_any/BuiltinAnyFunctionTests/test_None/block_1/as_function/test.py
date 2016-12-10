def test_function():
    try:
        print('>>> f = any')
        print('>>> x = None')
        print('>>> f(x)')
        f = any
        x = None
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()