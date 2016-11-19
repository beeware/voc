def test_function():
    try:
        print('>>> f = sum')
        print('>>> x = None')
        print('>>> f(x)')
        f = sum
        x = None
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()