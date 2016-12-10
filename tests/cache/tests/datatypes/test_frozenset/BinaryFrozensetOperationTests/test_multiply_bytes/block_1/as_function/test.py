def test_function():
    try:
        print('>>> x = frozenset()')
        print('>>> y = b""')
        print('>>> x * y')
        x = frozenset()
        y = b""
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset()')
        print('>>> y = b"This is another string of bytes"')
        print('>>> x * y')
        x = frozenset()
        y = b"This is another string of bytes"
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = b""')
        print('>>> x * y')
        x = frozenset({1, 2.3456, "another"})
        y = b""
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = b"This is another string of bytes"')
        print('>>> x * y')
        x = frozenset({1, 2.3456, "another"})
        y = b"This is another string of bytes"
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()