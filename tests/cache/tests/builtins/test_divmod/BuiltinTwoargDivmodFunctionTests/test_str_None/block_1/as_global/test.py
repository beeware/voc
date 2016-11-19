try:
    print('>>> f = divmod')
    print('>>> x = ""')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = divmod
    x = ""
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = "3"')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = divmod
    x = "3"
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = "This is another string"')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = divmod
    x = "This is another string"
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = divmod
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = "One arg: %s"')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = divmod
    x = "One arg: %s"
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = divmod
    x = "Three args: %s | %s | %s"
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
