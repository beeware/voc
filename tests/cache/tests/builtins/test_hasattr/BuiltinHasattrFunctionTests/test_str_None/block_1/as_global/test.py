try:
    print('>>> f = hasattr')
    print('>>> x = ""')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = hasattr
    x = ""
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = "3"')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = hasattr
    x = "3"
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = "This is another string"')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = hasattr
    x = "This is another string"
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = hasattr
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = "One arg: %s"')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = hasattr
    x = "One arg: %s"
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = hasattr
    x = "Three args: %s | %s | %s"
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
