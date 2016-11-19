def test_function():
    try:
        print('>>> f = chr')
        print('>>> x = set()')
        print('>>> f(x)')
        f = chr
        x = set()
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = chr')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> f(x)')
        f = chr
        x = {1, 2.3456, "another"}
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()