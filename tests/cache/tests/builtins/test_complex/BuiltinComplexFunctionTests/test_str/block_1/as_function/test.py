def test_function():
    try:
        print('>>> f = complex')
        print('>>> x = ""')
        print('>>> f(x)')
        f = complex
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = complex')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = complex
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = complex')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = complex
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = complex')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = complex
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = complex')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = complex
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = complex')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = complex
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()