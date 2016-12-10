try:
    print('>>> f = divmod')
    print('>>> x = NotImplemented')
    print('>>> y = ""')
    print('>>> f(x, y)')
    f = divmod
    x = NotImplemented
    y = ""
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = NotImplemented')
    print('>>> y = "3"')
    print('>>> f(x, y)')
    f = divmod
    x = NotImplemented
    y = "3"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = NotImplemented')
    print('>>> y = "This is another string"')
    print('>>> f(x, y)')
    f = divmod
    x = NotImplemented
    y = "This is another string"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = NotImplemented')
    print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x, y)')
    f = divmod
    x = NotImplemented
    y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = NotImplemented')
    print('>>> y = "One arg: %s"')
    print('>>> f(x, y)')
    f = divmod
    x = NotImplemented
    y = "One arg: %s"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = NotImplemented')
    print('>>> y = "Three args: %s | %s | %s"')
    print('>>> f(x, y)')
    f = divmod
    x = NotImplemented
    y = "Three args: %s | %s | %s"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
