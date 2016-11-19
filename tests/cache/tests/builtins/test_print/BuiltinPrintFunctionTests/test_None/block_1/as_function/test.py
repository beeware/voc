def test_function():
    try:
        print('>>> f = print')
        print('>>> x = None')
        print('>>> f(x)')
        f = print
        x = None
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()