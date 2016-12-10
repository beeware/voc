def test_function():
    try:
        print('>>> f = complex')
        print('>>> x = set()')
        print('>>> f(x)')
        f = complex
        x = set()
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = complex')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> f(x)')
        f = complex
        x = {1, 2.3456, "another"}
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()