def test_function():
    try:
        print('>>> f = hasattr')
        print('>>> x = b""')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = hasattr
        x = b""
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = b""')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = hasattr
        x = b""
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = hasattr
        x = b"This is another string of bytes"
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = hasattr
        x = b"This is another string of bytes"
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()