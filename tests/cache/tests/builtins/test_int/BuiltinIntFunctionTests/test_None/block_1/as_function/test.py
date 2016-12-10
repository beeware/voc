def test_function():
    try:
        print('>>> f = int')
        print('>>> x = None')
        print('>>> f(x)')
        f = int
        x = None
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()