try:
    print('>>> x = None')
    print('>>> y = ""')
    print('>>> x //= y')
    print('>>> x')
    x = None
    y = ""
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = "3"')
    print('>>> x //= y')
    print('>>> x')
    x = None
    y = "3"
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = "This is another string"')
    print('>>> x //= y')
    print('>>> x')
    x = None
    y = "This is another string"
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> x //= y')
    print('>>> x')
    x = None
    y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = "One arg: %s"')
    print('>>> x //= y')
    print('>>> x')
    x = None
    y = "One arg: %s"
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = "Three args: %s | %s | %s"')
    print('>>> x //= y')
    print('>>> x')
    x = None
    y = "Three args: %s | %s | %s"
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
