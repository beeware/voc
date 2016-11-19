def test_function():
    try:
        print('>>> x = NotImplemented')
        print('>>> y = type(1)')
        print('>>> x **= y')
        print('>>> x')
        x = NotImplemented
        y = type(1)
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = type("a")')
        print('>>> x **= y')
        print('>>> x')
        x = NotImplemented
        y = type("a")
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = type(object())')
        print('>>> x **= y')
        print('>>> x')
        x = NotImplemented
        y = type(object())
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x **= y')
        print('>>> x')
        x = NotImplemented
        y = type("MyClass", (object,), {})
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()