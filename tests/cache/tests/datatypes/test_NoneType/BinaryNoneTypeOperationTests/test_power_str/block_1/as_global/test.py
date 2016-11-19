try:
    print('>>> x = None')
    print('>>> y = ""')
    print('>>> x ** y')
    x = None
    y = ""
    print(x ** y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = "3"')
    print('>>> x ** y')
    x = None
    y = "3"
    print(x ** y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = "This is another string"')
    print('>>> x ** y')
    x = None
    y = "This is another string"
    print(x ** y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> x ** y')
    x = None
    y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(x ** y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = "One arg: %s"')
    print('>>> x ** y')
    x = None
    y = "One arg: %s"
    print(x ** y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = "Three args: %s | %s | %s"')
    print('>>> x ** y')
    x = None
    y = "Three args: %s | %s | %s"
    print(x ** y)
except Exception as e:
    print(type(e), ':', e)
print()
