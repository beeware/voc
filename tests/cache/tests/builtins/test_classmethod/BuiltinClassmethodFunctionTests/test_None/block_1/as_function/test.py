def test_function():
    try:
        print('>>> f = classmethod')
        print('>>> x = None')
        print('>>> f(x)')
        f = classmethod
        x = None
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()