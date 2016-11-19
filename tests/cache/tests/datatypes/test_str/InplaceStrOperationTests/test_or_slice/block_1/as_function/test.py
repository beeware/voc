def test_function():
    try:
        print('>>> x = ""')
        print('>>> y = slice(0)')
        print('>>> x |= y')
        print('>>> x')
        x = ""
        y = slice(0)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ""')
        print('>>> y = slice(5)')
        print('>>> x |= y')
        print('>>> x')
        x = ""
        y = slice(5)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ""')
        print('>>> y = slice(2, 7)')
        print('>>> x |= y')
        print('>>> x')
        x = ""
        y = slice(2, 7)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ""')
        print('>>> y = slice(2, 7, 2)')
        print('>>> x |= y')
        print('>>> x')
        x = ""
        y = slice(2, 7, 2)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ""')
        print('>>> y = slice(7, 2, -1)')
        print('>>> x |= y')
        print('>>> x')
        x = ""
        y = slice(7, 2, -1)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ""')
        print('>>> y = slice(7, 2, -2)')
        print('>>> x |= y')
        print('>>> x')
        x = ""
        y = slice(7, 2, -2)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "3"')
        print('>>> y = slice(0)')
        print('>>> x |= y')
        print('>>> x')
        x = "3"
        y = slice(0)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "3"')
        print('>>> y = slice(5)')
        print('>>> x |= y')
        print('>>> x')
        x = "3"
        y = slice(5)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "3"')
        print('>>> y = slice(2, 7)')
        print('>>> x |= y')
        print('>>> x')
        x = "3"
        y = slice(2, 7)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "3"')
        print('>>> y = slice(2, 7, 2)')
        print('>>> x |= y')
        print('>>> x')
        x = "3"
        y = slice(2, 7, 2)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "3"')
        print('>>> y = slice(7, 2, -1)')
        print('>>> x |= y')
        print('>>> x')
        x = "3"
        y = slice(7, 2, -1)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "3"')
        print('>>> y = slice(7, 2, -2)')
        print('>>> x |= y')
        print('>>> x')
        x = "3"
        y = slice(7, 2, -2)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "This is another string"')
        print('>>> y = slice(0)')
        print('>>> x |= y')
        print('>>> x')
        x = "This is another string"
        y = slice(0)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "This is another string"')
        print('>>> y = slice(5)')
        print('>>> x |= y')
        print('>>> x')
        x = "This is another string"
        y = slice(5)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "This is another string"')
        print('>>> y = slice(2, 7)')
        print('>>> x |= y')
        print('>>> x')
        x = "This is another string"
        y = slice(2, 7)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "This is another string"')
        print('>>> y = slice(2, 7, 2)')
        print('>>> x |= y')
        print('>>> x')
        x = "This is another string"
        y = slice(2, 7, 2)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "This is another string"')
        print('>>> y = slice(7, 2, -1)')
        print('>>> x |= y')
        print('>>> x')
        x = "This is another string"
        y = slice(7, 2, -1)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "This is another string"')
        print('>>> y = slice(7, 2, -2)')
        print('>>> x |= y')
        print('>>> x')
        x = "This is another string"
        y = slice(7, 2, -2)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = slice(0)')
        print('>>> x |= y')
        print('>>> x')
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = slice(0)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = slice(5)')
        print('>>> x |= y')
        print('>>> x')
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = slice(5)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = slice(2, 7)')
        print('>>> x |= y')
        print('>>> x')
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = slice(2, 7)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = slice(2, 7, 2)')
        print('>>> x |= y')
        print('>>> x')
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = slice(2, 7, 2)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = slice(7, 2, -1)')
        print('>>> x |= y')
        print('>>> x')
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = slice(7, 2, -1)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = slice(7, 2, -2)')
        print('>>> x |= y')
        print('>>> x')
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = slice(7, 2, -2)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "One arg: %s"')
        print('>>> y = slice(0)')
        print('>>> x |= y')
        print('>>> x')
        x = "One arg: %s"
        y = slice(0)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "One arg: %s"')
        print('>>> y = slice(5)')
        print('>>> x |= y')
        print('>>> x')
        x = "One arg: %s"
        y = slice(5)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "One arg: %s"')
        print('>>> y = slice(2, 7)')
        print('>>> x |= y')
        print('>>> x')
        x = "One arg: %s"
        y = slice(2, 7)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "One arg: %s"')
        print('>>> y = slice(2, 7, 2)')
        print('>>> x |= y')
        print('>>> x')
        x = "One arg: %s"
        y = slice(2, 7, 2)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "One arg: %s"')
        print('>>> y = slice(7, 2, -1)')
        print('>>> x |= y')
        print('>>> x')
        x = "One arg: %s"
        y = slice(7, 2, -1)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "One arg: %s"')
        print('>>> y = slice(7, 2, -2)')
        print('>>> x |= y')
        print('>>> x')
        x = "One arg: %s"
        y = slice(7, 2, -2)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = slice(0)')
        print('>>> x |= y')
        print('>>> x')
        x = "Three args: %s | %s | %s"
        y = slice(0)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = slice(5)')
        print('>>> x |= y')
        print('>>> x')
        x = "Three args: %s | %s | %s"
        y = slice(5)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = slice(2, 7)')
        print('>>> x |= y')
        print('>>> x')
        x = "Three args: %s | %s | %s"
        y = slice(2, 7)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = slice(2, 7, 2)')
        print('>>> x |= y')
        print('>>> x')
        x = "Three args: %s | %s | %s"
        y = slice(2, 7, 2)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = slice(7, 2, -1)')
        print('>>> x |= y')
        print('>>> x')
        x = "Three args: %s | %s | %s"
        y = slice(7, 2, -1)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = slice(7, 2, -2)')
        print('>>> x |= y')
        print('>>> x')
        x = "Three args: %s | %s | %s"
        y = slice(7, 2, -2)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()