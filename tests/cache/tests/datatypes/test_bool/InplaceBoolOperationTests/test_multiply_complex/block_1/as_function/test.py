def test_function():
    try:
        print('>>> x = True')
        print('>>> y = 1j')
        print('>>> x *= y')
        print('>>> x')
        x = True
        y = 1j
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = 3.14159265j')
        print('>>> x *= y')
        print('>>> x')
        x = True
        y = 3.14159265j
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = 1+2j')
        print('>>> x *= y')
        print('>>> x')
        x = True
        y = 1+2j
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = 3-4j')
        print('>>> x *= y')
        print('>>> x')
        x = True
        y = 3-4j
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = -5j')
        print('>>> x *= y')
        print('>>> x')
        x = True
        y = -5j
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = 1j')
        print('>>> x *= y')
        print('>>> x')
        x = False
        y = 1j
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = 3.14159265j')
        print('>>> x *= y')
        print('>>> x')
        x = False
        y = 3.14159265j
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = 1+2j')
        print('>>> x *= y')
        print('>>> x')
        x = False
        y = 1+2j
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = 3-4j')
        print('>>> x *= y')
        print('>>> x')
        x = False
        y = 3-4j
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = -5j')
        print('>>> x *= y')
        print('>>> x')
        x = False
        y = -5j
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()