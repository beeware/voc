def test_function():
    try:
        print('>>> x = slice(0)')
        print('>>> ~x')
        x = slice(0)
        print(~x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = slice(5)')
        print('>>> ~x')
        x = slice(5)
        print(~x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = slice(2, 7)')
        print('>>> ~x')
        x = slice(2, 7)
        print(~x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = slice(2, 7, 2)')
        print('>>> ~x')
        x = slice(2, 7, 2)
        print(~x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = slice(7, 2, -1)')
        print('>>> ~x')
        x = slice(7, 2, -1)
        print(~x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = slice(7, 2, -2)')
        print('>>> ~x')
        x = slice(7, 2, -2)
        print(~x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()