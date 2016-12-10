try:
    print('>>> x = ""')
    print('>>> y = None')
    print('>>> x //= y')
    print('>>> x')
    x = ""
    y = None
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "3"')
    print('>>> y = None')
    print('>>> x //= y')
    print('>>> x')
    x = "3"
    y = None
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "This is another string"')
    print('>>> y = None')
    print('>>> x //= y')
    print('>>> x')
    x = "This is another string"
    y = None
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> y = None')
    print('>>> x //= y')
    print('>>> x')
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    y = None
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "One arg: %s"')
    print('>>> y = None')
    print('>>> x //= y')
    print('>>> x')
    x = "One arg: %s"
    y = None
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> y = None')
    print('>>> x //= y')
    print('>>> x')
    x = "Three args: %s | %s | %s"
    y = None
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
