try:
    print('>>> x = ""')
    print('>>> y = NotImplemented')
    print('>>> x *= y')
    print('>>> x')
    x = ""
    y = NotImplemented
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "3"')
    print('>>> y = NotImplemented')
    print('>>> x *= y')
    print('>>> x')
    x = "3"
    y = NotImplemented
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "This is another string"')
    print('>>> y = NotImplemented')
    print('>>> x *= y')
    print('>>> x')
    x = "This is another string"
    y = NotImplemented
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> y = NotImplemented')
    print('>>> x *= y')
    print('>>> x')
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    y = NotImplemented
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "One arg: %s"')
    print('>>> y = NotImplemented')
    print('>>> x *= y')
    print('>>> x')
    x = "One arg: %s"
    y = NotImplemented
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> y = NotImplemented')
    print('>>> x *= y')
    print('>>> x')
    x = "Three args: %s | %s | %s"
    y = NotImplemented
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
