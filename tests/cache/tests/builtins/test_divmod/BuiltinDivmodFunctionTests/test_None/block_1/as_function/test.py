def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = None')
        print('>>> f(x)')
        f = divmod
        x = None
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()