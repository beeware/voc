try:
    print('>>> f = pow')
    print('>>> x = ""')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = pow
    x = ""
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = "3"')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = pow
    x = "3"
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = "This is another string"')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = pow
    x = "This is another string"
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = pow
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = "One arg: %s"')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = pow
    x = "One arg: %s"
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = pow
    x = "Three args: %s | %s | %s"
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
