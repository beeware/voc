def test_function():
    try:
        print('>>> f = memoryview')
        print('>>> x = True')
        print('>>> f(x)')
        f = memoryview
        x = True
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = memoryview')
        print('>>> x = False')
        print('>>> f(x)')
        f = memoryview
        x = False
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()