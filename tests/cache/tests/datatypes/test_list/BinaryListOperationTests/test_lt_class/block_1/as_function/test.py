def test_function():
    try:
        print('>>> x = []')
        print('>>> y = type(1)')
        print('>>> x < y')
        x = []
        y = type(1)
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = []')
        print('>>> y = type("a")')
        print('>>> x < y')
        x = []
        y = type("a")
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = []')
        print('>>> y = type(object())')
        print('>>> x < y')
        x = []
        y = type(object())
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = []')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x < y')
        x = []
        y = type("MyClass", (object,), {})
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> y = type(1)')
        print('>>> x < y')
        x = [3, 4, 5]
        y = type(1)
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> y = type("a")')
        print('>>> x < y')
        x = [3, 4, 5]
        y = type("a")
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> y = type(object())')
        print('>>> x < y')
        x = [3, 4, 5]
        y = type(object())
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x < y')
        x = [3, 4, 5]
        y = type("MyClass", (object,), {})
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = type(1)')
        print('>>> x < y')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = type(1)
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = type("a")')
        print('>>> x < y')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = type("a")
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = type(object())')
        print('>>> x < y')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = type(object())
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x < y')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = type("MyClass", (object,), {})
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> y = type(1)')
        print('>>> x < y')
        x = ["a","b","c"]
        y = type(1)
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> y = type("a")')
        print('>>> x < y')
        x = ["a","b","c"]
        y = type("a")
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> y = type(object())')
        print('>>> x < y')
        x = ["a","b","c"]
        y = type(object())
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x < y')
        x = ["a","b","c"]
        y = type("MyClass", (object,), {})
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()