try:
    print('>>> f = getattr')
    print('>>> x = ""')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = getattr
    x = ""
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = "3"')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = getattr
    x = "3"
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = "This is another string"')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = getattr
    x = "This is another string"
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = getattr
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = "One arg: %s"')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = getattr
    x = "One arg: %s"
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = getattr
    x = "Three args: %s | %s | %s"
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
