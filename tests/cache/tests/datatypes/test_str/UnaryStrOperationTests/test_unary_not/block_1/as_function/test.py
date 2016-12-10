def test_function():
    try:
        print('>>> x = ""')
        print('>>> not x')
        x = ""
        print(not x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "3"')
        print('>>> not x')
        x = "3"
        print(not x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "This is another string"')
        print('>>> not x')
        x = "This is another string"
        print(not x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> not x')
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(not x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "One arg: %s"')
        print('>>> not x')
        x = "One arg: %s"
        print(not x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> not x')
        x = "Three args: %s | %s | %s"
        print(not x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()