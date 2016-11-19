def test_function():
    try:
        print('>>> x = frozenset()')
        print('>>> not x')
        x = frozenset()
        print(not x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> not x')
        x = frozenset({1, 2.3456, "another"})
        print(not x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()