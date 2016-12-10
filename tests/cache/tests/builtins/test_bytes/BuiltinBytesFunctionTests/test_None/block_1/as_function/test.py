def test_function():
    try:
        print('>>> f = bytes')
        print('>>> x = None')
        print('>>> f(x)')
        f = bytes
        x = None
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()