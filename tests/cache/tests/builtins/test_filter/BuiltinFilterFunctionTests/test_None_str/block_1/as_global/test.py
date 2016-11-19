try:
    print('>>> f = filter')
    print('>>> x = None')
    print('>>> y = ""')
    print('>>> f(x, y)')
    f = filter
    x = None
    y = ""
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = None')
    print('>>> y = "3"')
    print('>>> f(x, y)')
    f = filter
    x = None
    y = "3"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = None')
    print('>>> y = "This is another string"')
    print('>>> f(x, y)')
    f = filter
    x = None
    y = "This is another string"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = None')
    print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x, y)')
    f = filter
    x = None
    y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = None')
    print('>>> y = "One arg: %s"')
    print('>>> f(x, y)')
    f = filter
    x = None
    y = "One arg: %s"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = None')
    print('>>> y = "Three args: %s | %s | %s"')
    print('>>> f(x, y)')
    f = filter
    x = None
    y = "Three args: %s | %s | %s"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
