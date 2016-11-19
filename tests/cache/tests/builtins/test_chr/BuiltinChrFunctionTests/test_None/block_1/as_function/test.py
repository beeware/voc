def test_function():
    try:
        print('>>> f = chr')
        print('>>> x = None')
        print('>>> f(x)')
        f = chr
        x = None
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()