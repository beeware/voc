def test_function():
    try:
        print('>>> x = True')
        print('>>> y = ""')
        print('>>> x &= y')
        print('>>> x')
        x = True
        y = ""
        x &= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = "3"')
        print('>>> x &= y')
        print('>>> x')
        x = True
        y = "3"
        x &= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = "This is another string"')
        print('>>> x &= y')
        print('>>> x')
        x = True
        y = "This is another string"
        x &= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> x &= y')
        print('>>> x')
        x = True
        y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        x &= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = "One arg: %s"')
        print('>>> x &= y')
        print('>>> x')
        x = True
        y = "One arg: %s"
        x &= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = "Three args: %s | %s | %s"')
        print('>>> x &= y')
        print('>>> x')
        x = True
        y = "Three args: %s | %s | %s"
        x &= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = ""')
        print('>>> x &= y')
        print('>>> x')
        x = False
        y = ""
        x &= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = "3"')
        print('>>> x &= y')
        print('>>> x')
        x = False
        y = "3"
        x &= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = "This is another string"')
        print('>>> x &= y')
        print('>>> x')
        x = False
        y = "This is another string"
        x &= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> x &= y')
        print('>>> x')
        x = False
        y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        x &= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = "One arg: %s"')
        print('>>> x &= y')
        print('>>> x')
        x = False
        y = "One arg: %s"
        x &= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = "Three args: %s | %s | %s"')
        print('>>> x &= y')
        print('>>> x')
        x = False
        y = "Three args: %s | %s | %s"
        x &= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()