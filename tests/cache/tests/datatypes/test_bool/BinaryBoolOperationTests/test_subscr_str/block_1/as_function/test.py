def test_function():
    try:
        print('>>> x = True')
        print('>>> y = ""')
        print('>>> x[y]')
        x = True
        y = ""
        print(x[y])
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = "3"')
        print('>>> x[y]')
        x = True
        y = "3"
        print(x[y])
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = "This is another string"')
        print('>>> x[y]')
        x = True
        y = "This is another string"
        print(x[y])
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> x[y]')
        x = True
        y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(x[y])
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = "One arg: %s"')
        print('>>> x[y]')
        x = True
        y = "One arg: %s"
        print(x[y])
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = "Three args: %s | %s | %s"')
        print('>>> x[y]')
        x = True
        y = "Three args: %s | %s | %s"
        print(x[y])
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = ""')
        print('>>> x[y]')
        x = False
        y = ""
        print(x[y])
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = "3"')
        print('>>> x[y]')
        x = False
        y = "3"
        print(x[y])
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = "This is another string"')
        print('>>> x[y]')
        x = False
        y = "This is another string"
        print(x[y])
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> x[y]')
        x = False
        y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(x[y])
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = "One arg: %s"')
        print('>>> x[y]')
        x = False
        y = "One arg: %s"
        print(x[y])
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = "Three args: %s | %s | %s"')
        print('>>> x[y]')
        x = False
        y = "Three args: %s | %s | %s"
        print(x[y])
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()