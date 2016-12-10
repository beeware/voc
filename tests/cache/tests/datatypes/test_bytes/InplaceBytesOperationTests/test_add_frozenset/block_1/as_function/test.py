def test_function():
    try:
        print('>>> x = b""')
        print('>>> y = frozenset()')
        print('>>> x += y')
        print('>>> x')
        x = b""
        y = frozenset()
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x += y')
        print('>>> x')
        x = b""
        y = frozenset({1, 2.3456, "another"})
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = frozenset()')
        print('>>> x += y')
        print('>>> x')
        x = b"This is another string of bytes"
        y = frozenset()
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x += y')
        print('>>> x')
        x = b"This is another string of bytes"
        y = frozenset({1, 2.3456, "another"})
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()